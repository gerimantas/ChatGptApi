import json
import os

STRATEGY_FILE = "Co/strategy/progress_tracking.json"

def load_strategy():
    """Įkelia strategijos progreso failą."""
    if not os.path.exists(STRATEGY_FILE):
        return {}
    with open(STRATEGY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_strategy(strategy_data):
    """Išsaugo strategijos progreso duomenis."""
    with open(STRATEGY_FILE, "w", encoding="utf-8") as file:
        json.dump(strategy_data, file, indent=4)

def update_progress(task, status):
    """Atnaujina strategijos užduoties būseną."""
    strategy = load_strategy()
    strategy[task] = status
    save_strategy(strategy)

if __name__ == "__main__":
    print("📌 Strategy Tracker: Naudokite šią funkciją strategijos progresui valdyti.")
