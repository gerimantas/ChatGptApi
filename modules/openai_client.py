import openai
import logging
import aiosqlite
import asyncio
from cachetools import LRUCache
from tenacity import retry, stop_after_attempt, wait_exponential
from logging.handlers import RotatingFileHandler
from ai.assist.core.config import load_config
import os


# ✅ Įkeliame konfigūraciją
config = load_config()

# ✅ Sukuriame OpenAI klientą
client = openai.AsyncOpenAI(api_key=config["openai_api_key"])

# ✅ Nustatoma logų sistema
if not os.path.exists(config["log_dir"]):
    os.makedirs(config["log_dir"])

LOG_FILE = f"{config['log_dir']}/openai_client_errors.log"
handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=5)
logging.basicConfig(level=logging.ERROR, handlers=[handler],
                    format="%(asctime)s - %(levelname)s - %(message)s")

# ✅ Sukuriame LRU cache
cache = LRUCache(maxsize=config["lru_cache_size"])


async def ensure_cache():
    """Asinchroniškai sukuria cache DB jei jos nėra."""
    os.makedirs(os.path.dirname(config["cache_file"]), exist_ok=True)
    async with aiosqlite.connect(config["cache_file"]) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS cache (
                prompt TEXT PRIMARY KEY,
                response TEXT
            )
        """)
        await db.commit()


@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=10))
async def ask_openai(prompt):
    """Asinchroniškai siunčia užklausą OpenAI API su LRU cache, SQLite ir automatiniu backoff."""
    try:
        # ✅ Pirmiausia tikriname LRU cache
        if prompt in cache:
            print("💾 Atsakymas paimtas iš LRU cache!")
            return cache[prompt]

        # ✅ Jei nėra LRU cache, tikriname SQLite cache
        async with aiosqlite.connect(config["cache_file"]) as db:
            async with db.execute("SELECT response FROM cache WHERE prompt=?", (prompt,)) as cursor:
                row = await cursor.fetchone()
                if row:
                    print("💾 Atsakymas paimtas iš SQLite cache!")
                    cache[prompt] = row[0]  # Įdedame į LRU cache
                    return row[0]

        # ✅ Jei atsakymo nėra cache, siunčiame užklausą OpenAI API
        response = await client.chat.completions.create(
            model=config["model"],
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content

        # ✅ Išsaugome į LRU cache
        cache[prompt] = result

        # ✅ Išsaugome į SQLite cache
        async with aiosqlite.connect(config["cache_file"]) as db:
            await db.execute(
                "INSERT OR REPLACE INTO cache (prompt, response) VALUES (?, ?)", (prompt, result)
            )
            await db.commit()

        return result

    except openai.OpenAIError as e:
        logging.error(f"OpenAI API klaida: {e}")
        return None


# ✅ Paleidžiame `ensure_cache()` paleidžiant programą
asyncio.run(ensure_cache())
