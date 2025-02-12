import json
import os

CONFIG_FILE = "config.json"

def load_config():
    """Įkelia boto nustatymus iš `config.json`. Jei failas neegzistuoja, sukuria su numatytosiomis reikšmėmis."""
    if not os.path.exists(CONFIG_FILE):
        default_config = {
            "model": "gpt-4o",
            "language": "auto",
            "response_detail": 3
        }
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(default_config, f, ensure_ascii=False, indent=4)
        return default_config

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def update_config(key, value):
    """Atnaujina konkretų nustatymą ir išsaugo jį."""
    config = load_config()
    config[key] = value
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=4)
    return True
