import openai
import os
import time
import logging
import shelve
import asyncio
from dotenv import load_dotenv

# Įkeliame API raktą iš .env failo
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Sukuriamas OpenAI klientas
client = openai.AsyncOpenAI(api_key=OPENAI_API_KEY)

# Sukuriami aplankai, jei jų nėra
LOG_DIR = "logs"
CACHE_DIR = "cache"
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

# Nustatoma logų sistema
LOG_FILE = os.path.join(LOG_DIR, "openai_client.log")
logging.basicConfig(filename=LOG_FILE, level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Cache failas
CACHE_FILE = os.path.join(CACHE_DIR, "openai_cache.db")

async def ask_openai(prompt, model="gpt-4o", max_retries=5):
    """Asinchroniškai siunčia užklausą OpenAI API su caching ir backoff retry mechanizmu."""
    retries = 0
    wait_time = 1  # Pradinis laukimo laikas sekundėmis

    with shelve.open(CACHE_FILE) as cache:
        if prompt in cache:
            print("💾 Atsakymas paimtas iš cache!")
            return cache[prompt]

        while retries < max_retries:
            try:
                response = await client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}]
                )
                result = response.choices[0].message.content
                cache[prompt] = result
                return result

            except openai.RateLimitError:
                logging.error("RateLimitError: API pasiekė užklausų ribą.")
                print(f"⚠️ API pasiekė užklausų ribą. Laukiama {wait_time} sek. ir bandoma dar kartą...")
                await asyncio.sleep(wait_time)
                wait_time *= 2
                retries += 1
            
            except openai.APITimeoutError:
                logging.error("TimeoutError: API atsako per ilgai.")
                print(f"⏳ API atsako per ilgai. Laukiama {wait_time} sek. ir bandoma dar kartą...")
                await asyncio.sleep(wait_time)
                wait_time *= 2
                retries += 1

            except openai.OpenAIError as e:
                logging.error(f"OpenAIError: {e}")
                print(f"⚠️ OpenAI API klaida: {e}")
                return None

        logging.error("Nepavyko gauti atsakymo po kelių bandymų.")
        print("🚫 Nepavyko gauti atsakymo po kelių bandymų.")
        return None

async def send_message_to_gpt(messages):
    """Asinchroniškai siunčia žinutę į OpenAI API ir grąžina atsakymą."""
    return await ask_openai(messages[0]["content"])
