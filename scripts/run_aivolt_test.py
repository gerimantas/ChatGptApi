import json
import os

# Nustatome testinės užduoties failo kelią
TASK_FILE = "C:/Users/37065/Projects/ai.assist/tests/aivolt_test_task.json"

# Tikriname, ar failas egzistuoja
if not os.path.exists(TASK_FILE):
    print(f"❌ Klaida: Testo failas nerastas: {TASK_FILE}")
    exit(1)

# Įkeliame testavimo užduotį
with open(TASK_FILE, "r", encoding="utf-8") as file:
    test_task = json.load(file)

print("🚀 Aivolt testavimo užduotis pradėta...")
print(f"📌 Užduotis: {test_task['TASK_NAME']}")
print(f"📄 Aprašymas: {test_task['DESCRIPTION']}")
print(f"🤖 AI Rolė: {test_task['AI_ROLE']}")
print(f"🎯 Tikslinis modelis: {test_task['REQUIREMENTS']['NLP_MODEL']}")

# Simuliuojame užduoties vykdymą (čia turėtų būti integracija su AI modeliu)
for step in test_task["STEPS"]:
    print(f"🔹 Atliekamas žingsnis: {step}")

print("✅ Testas baigtas! Aivolt užduotis įvykdyta.")
