import aiosqlite
import os
import logging
import asyncio
from datetime import datetime, timedelta
from logging.handlers import RotatingFileHandler

DB_FILE = os.path.join(os.path.dirname(__file__), "api_usage.db")
LOG_FILE = os.path.join(os.path.dirname(__file__), "api_usage.log")

# ✅ Sukuriame logų sistemą su rotavimu
handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=5)
logging.basicConfig(level=logging.INFO, handlers=[handler],
                    format="%(asctime)s - %(levelname)s - %(message)s")

class APIUsageTracker:
    def __init__(self):
        asyncio.run(self.ensure_db())

    async def ensure_db(self):
        """Asinchroniškai sukuria SQLite DB, jei ji neegzistuoja."""
        async with aiosqlite.connect(DB_FILE) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS usage (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    tokens_used INTEGER
                )
            """)
            await db.commit()

    async def log_api_usage(self, tokens):
        """Asinchroniškai registruoja naują API užklausą ir naudojamus tokenus."""
        async with aiosqlite.connect(DB_FILE) as db:
            await db.execute("INSERT INTO usage (timestamp, tokens_used) VALUES (?, ?)",
                             (datetime.now().isoformat(), tokens))
            await db.commit()

        log_message = f"🔹 API naudoti {tokens} tokenai."
        print(log_message)
        logging.info(log_message)

    async def get_total_usage(self):
        """Asinchroniškai grąžina bendrą sunaudotų tokenų kiekį."""
        async with aiosqlite.connect(DB_FILE) as db:
            async with db.execute("SELECT SUM(tokens_used) FROM usage") as cursor:
                row = await cursor.fetchone()
                return row[0] if row[0] is not None else 0

    async def check_usage_limits(self, limit=100000):
        """Patikrina, ar naudojimas neviršija nustatyto limito."""
        total_usage = await self.get_total_usage()
        if total_usage > limit:
            warning_message = "⚠️ Dėmesio! API sunaudotų tokenų kiekis viršijo nustatytą ribą!"
            print(warning_message)
            logging.warning(warning_message)

    async def reset_usage(self):
        """Asinchroniškai ištrina senesnius nei 30 dienų įrašus."""
        cutoff_date = (datetime.now() - timedelta(days=30)).isoformat()
        async with aiosqlite.connect(DB_FILE) as db:
            await db.execute("DELETE FROM usage WHERE timestamp < ?", (cutoff_date,))
            await db.commit()
        logging.info("✅ Senesni nei 30 dienų duomenys išvalyti.")

# ✅ Asinchroninis paleidimas
async def main():
    tracker = APIUsageTracker()
    await tracker.log_api_usage(500)
    await tracker.check_usage_limits()
    await tracker.reset_usage()

asyncio.run(main())
