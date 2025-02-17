import json
import os
from dotenv import load_dotenv

CONFIG_FILE = "config/ai_config.json"  # 🔄 Teisingas kelias!

def load_config():
    """Įkelia boto nustatymus iš `ai_config.json`. Jei failas neegzistuoja, sukuria jį su numatytosiomis reikšmėmis."""
    os.makedirs("config", exist_ok=True)  # 🔄 Užtikriname, kad katalogas egzistuoja

    if not os.path.exists(CONFIG_FILE):
        default_config = {
            "model": "gpt-4o",
            "language": "auto",
            "response_detail": 3,
            "cache_file": "cache/openai_cache.db",
            "log_dir": "logs",
            "openai_api_key": "",
            "lru_cache_size": 100
        }
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(default_config, f, ensure_ascii=False, indent=4)

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)

    # ✅ Įkeliamas OpenAI API raktas iš `.env`, jei jis nėra nurodytas `ai_config.json`
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY", "").strip()

    if not config.get("openai_api_key"):
        config["openai_api_key"] = api_key

    # ✅ Užtikriname, kad API raktas tikrai nebus tuščias
    if not config["openai_api_key"]:
        raise ValueError("❌ Klaida: OpenAI API raktas nėra nustatytas!")

    return config

def update_config(key, value):
    """Atnaujina konkretų nustatymą ir išsaugo jį JSON faile."""
    config = load_config()
    config[key] = value
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=4)
    return True
