import json
import os

TASK_FILE = "logs/task_entries.json"

def ensure_task_log():
    """Užtikrina, kad užduočių žurnalo failas egzistuoja."""
    if not os.path.exists("logs"):
        os.makedirs("logs")
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)

def collect_user_task():
    """Surinka vartotojo užduoties informaciją ir sugeneruoja projekto strategiją."""
    print("\n📝 Užduoties priėmimo anketa\n")

    task_title = input("🔹 Apibūdinkite užduotį (1 sakinys): ")
    task_description = input("🔹 Detalus užduoties aprašymas: ")
    expected_result = input("🔹 Koks norimas rezultatas? ")

    priority = input("🔹 Užduoties prioritetas (aukštas / vidutinis / žemas): ").lower()
    deadline = input("🔹 Iki kada turi būti įvykdyta? (YYYY-MM-DD) ")

    project_name = generate_project_name(task_title)
    
    task_entry = {
        "project_name": project_name,
        "task_title": task_title,
        "task_description": task_description,
        "expected_result": expected_result,
        "priority": priority,
        "deadline": deadline
    }
    
    save_task_entry(task_entry)
    
    print(f"\n✅ Užduotis priimta! Projektas: **{project_name}**")
    return task_entry

def generate_project_name(task_title):
    """Generuoja projekto pavadinimą pagal užduotį."""
    base_name = task_title.replace(" ", "_").lower()
    return f"project_{base_name}"

def save_task_entry(entry):
    """Išsaugo užduoties informaciją JSON faile."""
    ensure_task_log()
    with open(TASK_FILE, "r+", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
        data.append(entry)
        file.seek(0)
        json.dump(data, file, indent=4, ensure_ascii=False)
