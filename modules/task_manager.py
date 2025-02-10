import os
import re

PROJECT_PLAN_FILE = "project_plan.md"

def parse_project_plan():
    """Nuskaityti projekto planą ir išanalizuoti užduotis."""
    if not os.path.exists(PROJECT_PLAN_FILE):
        print("⚠️ Projekto planas nerastas!")
        return [], []
    
    done_tasks = []
    pending_tasks = []
    
    with open(PROJECT_PLAN_FILE, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(r"- \[(.)\] (.+)", line.strip())
            if match:
                status, task = match.groups()
                if status == "x":
                    done_tasks.append(task)
                else:
                    pending_tasks.append(task)
    
    return done_tasks, pending_tasks

def calculate_progress():
    """Apskaičiuoti atliktų darbų procentą."""
    done_tasks, pending_tasks = parse_project_plan()
    total_tasks = len(done_tasks) + len(pending_tasks)
    
    if total_tasks == 0:
        return 0.0
    
    progress = (len(done_tasks) / total_tasks) * 100
    return round(progress, 2)

def generate_progress_report():
    """Generuoti progreso ataskaitą."""
    done_tasks, pending_tasks = parse_project_plan()
    progress = calculate_progress()
    
    print("\n📊 **PROJEKTO PROGRESO ATASKAITA** 📊")
    print(f"✅ Atliktos užduotys: {len(done_tasks)}")
    print(f"⏳ Likusios užduotys: {len(pending_tasks)}")
    print(f"📈 Progresas: {progress}%")
    
    if pending_tasks:
        print("\n🔹 **Likusios užduotys:**")
        for task in pending_tasks:
            print(f"  - {task}")

if __name__ == "__main__":
    generate_progress_report()