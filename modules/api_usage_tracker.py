import json
import os
import logging
from datetime import datetime

API_USAGE_FILE = os.path.join(os.path.dirname(__file__), "api_usage_report.json")
LOG_FILE = os.path.join(os.path.dirname(__file__), "api_usage.log")

# Sukuriame log failą, jei jo nėra
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("")

# Konfigūruojame log failą
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class APIUsageTracker:
    def __init__(self):
        self.usage_data = self.load_usage_data()
    
    def load_usage_data(self):
        """Įkelia API naudojimo duomenis iš failo."""
        if os.path.exists(API_USAGE_FILE):
            with open(API_USAGE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"requests": 0, "tokens_used": 0, "history": []}
    
    def save_usage_data(self):
        """Išsaugo atnaujintus API naudojimo duomenis."""
        with open(API_USAGE_FILE, "w", encoding="utf-8") as f:
            json.dump(self.usage_data, f, ensure_ascii=False, indent=4)
    
    def log_api_usage(self, tokens):
        """Registruoja naują API užklausą ir naudojamus tokenus."""
        self.usage_data["requests"] += 1
        self.usage_data["tokens_used"] += tokens
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "tokens_used": tokens
        }
        self.usage_data["history"].append(log_entry)
        self.save_usage_data()
        
        log_message = f"🔹 API naudoti {tokens} tokenai. Iš viso: {self.usage_data['tokens_used']}"
        print(log_message)
        logging.info(log_message)
    
    def check_usage_limits(self, limit=100000):
        """Patikrina, ar naudojimas neviršija nustatyto limito."""
        if self.usage_data["tokens_used"] > limit:
            warning_message = "⚠️ Dėmesio! API sunaudotų tokenų kiekis viršijo nustatytą ribą!"
            print(warning_message)
            logging.warning(warning_message)
    
if __name__ == "__main__":
    tracker = APIUsageTracker()
    tracker.log_api_usage(500)
    tracker.check_usage_limits()
