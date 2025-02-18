import openai
import logging
import aiosqlite
import asyncio
import json
import os
from cachetools import LRUCache
from tenacity import retry, stop_after_attempt, wait_exponential
from logging.handlers import RotatingFileHandler

# ✅ Konfigūracijos failų keliai
CONFIG_FILES = ["config/ai_config.json", "config.json"]

def load_api_key():
    """Ieško OpenAI API rakto ai_config.json, config.json ir aplinkos kintamuosiuose."""
    api_key = None

    for config_file in CONFIG_FILES:
        if os.path.exists(config_file):
            try:
                with open(config_file, "r", encoding="utf-8") as file:
                    config = json.load(file)
                    api_key = config.get("openai_api_key") or api_key
            except (json.JSONDecodeError, IOError) as e:
                print(f"⚠️ Klaida skaitant {config_file}: {e}")

    # Jei API raktas dar nerastas, bandome aplinkos kintamąjį
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("❌ API raktas nerastas! Patikrink ai_config.json, config.json arba aplinkos kintamuosius.")

    return api_key

# ✅ Įkeliame API raktą
try:
    openai.api_key = load_api_key()
    print(f"🔍 Naudojamas API raktas: {openai.api_key}")  # Diagnostikos eilutė
except ValueError as e:
    print(e)

# ✅ Sukuriame OpenAI klientą
client = openai.AsyncOpenAI(api_key=openai.api_key)

# ✅ Logų sistema
LOG_FILE = "logs/openai_client_errors.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=5)
logging.basicConfig(level=logging.ERROR, handlers=[handler], format="%(asctime)s - %(levelname)s - %(message)s")

# ✅ Sukuriame LRU cache
cache = LRUCache(maxsize=100)

async def ensure_cache():
    """Asinchroniškai sukuria cache DB jei jos nėra."""
    os.makedirs("cache", exist_ok=True)
    async with aiosqlite.connect("cache/openai_cache.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS cache (
                prompt TEXT PRIMARY KEY,
                response TEXT
            )
        """)
        await db.commit()

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=10))
async def ask_openai(prompt):
    """Asinchroniškai siunčia užklausą OpenAI API su cache mechanizmu."""
    try:
        if prompt in cache:
            print("💾 Atsakymas paimtas iš cache!")
            return cache[prompt]

        async with aiosqlite.connect("cache/openai_cache.db") as db:
            async with db.execute("SELECT response FROM cache WHERE prompt=?", (prompt,)) as cursor:
                row = await cursor.fetchone()
                if row:
                    print("💾 Atsakymas paimtas iš SQLite cache!")
                    cache[prompt] = row[0]
                    return row[0]

        print(f"🔍 Naudojamas API raktas: {openai.api_key}")  # Diagnostikos eilutė prieš siunčiant užklausą

        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content

        cache[prompt] = result

        async with aiosqlite.connect("cache/openai_cache.db") as db:
            await db.execute("INSERT OR REPLACE INTO cache (prompt, response) VALUES (?, ?)", (prompt, result))
            await db.commit()

        return result

    except openai.OpenAIError as e:
        logging.error(f"OpenAI API klaida: {e}")
        return None

async def get_current_model():
    """Grąžina dabartinį OpenAI GPT modelio pavadinimą."""
    return "gpt-4o"

asyncio.run(ensure_cache())

__all__ = ["ask_openai", "get_current_model"]

