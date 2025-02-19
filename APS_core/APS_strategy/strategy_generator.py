import json
import os

STRATEGY_FILE = "logs/strategy_log.json"

def ensure_strategy_log():
    """Užtikrina, kad strategijos failas egzistuoja."""
    if not os.path.exists("logs"):
        os.makedirs("logs")
    if not os.path.exists(STRATEGY_FILE):
        with open(STRATEGY_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)

def generate_strategy(task_data):
    """Generuoja strategiją pagal užduoties duomenis."""
    
    strategy = {
        "project_name": task_data["project_name"],
        "goals": f"Sukuriamas sprendimas užduočiai: {task_data['task_title']}",
        "steps": [
            "1️⃣ Surinkti visus reikiamus duomenis",
            "2️⃣ Apibrėžti techninius reikalavimus",
            "3️⃣ Sukurti prototipą arba planą",
            "4️⃣ Atlikti testavimą ir koregavimus",
            "5️⃣ Įdiegti ir pristatyti rezultatą"
        ],
        "priority": task_data["priority"],
        "deadline": task_data["deadline"]
    }

    save_strategy(strategy)
    print("\n✅ Strategija sukurta ir išsaugota!")
    return strategy

def save_strategy(strategy):
    """Išsaugo strategiją JSON faile."""
    ensure_strategy_log()
    with open(STRATEGY_FILE, "r+", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
        data.append(strategy)
        file.seek(0)
        json.dump(data, file, indent=4, ensure_ascii=False)
