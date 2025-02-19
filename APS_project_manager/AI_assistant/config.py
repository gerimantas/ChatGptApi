import json
import os
from dotenv import load_dotenv

CONFIG_FILE = "config/ai_config.json"  # 🔄 Teisingas kelias!

DEFAULT_CONFIG = {
    "model": "gpt-4o",
    "language": "auto",
    "response_detail": 3,
    "cache_file": "cache/openai_cache.db",
    "log_dir": "logs",
    "openai_api_key": "",
    "lru_cache_size": 100
}

def load_config():
    """Įkelia boto nustatymus iš `ai_config.json`. Jei failas neegzistuoja, sukuria jį su numatytosiomis reikšmėmis."""
    os.makedirs("config", exist_ok=True)  # 🔄 Užtikriname, kad katalogas egzistuoja

    # Jei failas neegzistuoja, sukuriame naują su numatytosiomis reikšmėmis
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_CONFIG, f, ensure_ascii=False, indent=4)

    # Įkeliame konfigūraciją iš failo
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)

    # ✅ Užtikriname, kad visi laukeliai būtų užpildyti pagal `DEFAULT_CONFIG`
    for key, value in DEFAULT_CONFIG.items():
        config.setdefault(key, value)

    # ✅ Įkeliamas OpenAI API raktas iš `.env`, jei nėra nurodytas JSON faile
    load_dotenv()
    env_api_key = os.getenv("OPENAI_API_KEY", "").strip()

    if not config["openai_api_key"]:
        config["openai_api_key"] = env_api_key

    # ✅ Užtikriname, kad API raktas tikrai nebus tuščias
    if not config["openai_api_key"]:
        raise ValueError("❌ Klaida: OpenAI API raktas nėra nustatytas! Nustatykite jį `config/ai_config.json` arba `.env` faile.")

    return config

def update_config(key, value):
    """Atnaujina konkretų nustatymą ir išsaugo jį JSON faile."""
    config = load_config()
    config[key] = value
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=4)
    return True
