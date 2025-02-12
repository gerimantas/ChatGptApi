import openai
import os
import time
import logging
import shelve
import asyncio
from dotenv import load_dotenv
import sys
sys.stdout.reconfigure(encoding='utf-8')


# ✅ Įkeliame API raktą iš .env failo
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Sukuriamas OpenAI klientas
client = openai.AsyncOpenAI(api_key=OPENAI_API_KEY)

# ✅ Sukuriami aplankai, jei jų nėra
LOG_DIR = "logs"
CACHE_DIR = "cache"

def ensure_cache_directory():
    """Užtikrina, kad `cache/` katalogas egzistuoja prieš naudojant cache failą."""
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
        print("🛠️ Sukurtas `cache/` katalogas.")

ensure_cache_directory()

# ✅ Nustatoma logų sistema
LOG_FILE = os.path.join(LOG_DIR, "openai_client.log")
logging.basicConfig(filename=LOG_FILE, level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# ✅ Cache failas
CACHE_FILE = os.path.join(CACHE_DIR, "openai_cache.db")

async def get_current_model():
    """Užklausia OpenAI API ir grąžina tikrą GPT modelio versiją, kuri realiai naudojama."""
    ensure_cache_directory()
    try:
        response = await client.chat.completions.create(
            model="gpt-4o",  # Naudojame paskutinį patvirtintą modelį, nes užklausa be `model` nesuveiks
            messages=[{"role": "system", "content": "Grąžink tik modelio versijos pavadinimą."}]
        )
        return response.model  # OpenAI API grąžina `model` lauką su tiksliu modelio pavadinimu
    except Exception as e:
        print(f"⚠️ Klaida gaunant realų modelio pavadinimą: {e}")
        return "Nežinoma versija"

async def ask_openai(prompt, max_retries=5):
    """Asinchroniškai siunčia užklausą OpenAI API su caching ir backoff retry mechanizmu."""
    ensure_cache_directory()
    retries = 0
    wait_time = 1  # Pradinis laukimo laikas sekundėmis

    try:
        with shelve.open(CACHE_FILE) as cache:
            if prompt in cache:
                print("💾 Atsakymas paimtas iš cache!")
                return cache[prompt]

            while retries < max_retries:
                try:
                    response = await client.chat.completions.create(
                        model="gpt-4o",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    result = response.choices[0].message.content.encode("utf-8", errors="replace").decode("utf-8")
                    cache[prompt] = result
                    return result

                except openai.RateLimitError:
                    print(f"⚠️ API pasiekė užklausų ribą. Laukiama {wait_time} sek. ir bandoma dar kartą...")
                    await asyncio.sleep(wait_time)
                    wait_time *= 2
                    retries += 1
                
                except openai.APITimeoutError:
                    print(f"⏳ API atsako per ilgai. Laukiama {wait_time} sek. ir bandoma dar kartą...")
                    await asyncio.sleep(wait_time)
                    wait_time *= 2
                    retries += 1

                except openai.OpenAIError as e:
                    print(f"⚠️ OpenAI API klaida: {e}")
                    return None

            print("🚫 Nepavyko gauti atsakymo po kelių bandymų.")
            return None

    except Exception:
        print("⚠️ Cache failas sugadintas. Jis bus ištrintas ir atkurtas.")
        return None
