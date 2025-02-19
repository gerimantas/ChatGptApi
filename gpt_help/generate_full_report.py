import os
import json
import datetime
import subprocess

GPT_HELP_DIR = "C:/Users/37065/Projects/ai.assist/gpt_help/"
SESSION_REPORT = os.path.join(GPT_HELP_DIR, "session_report.txt")

FILES = {
    "progress_summary.txt": "🔹 Projekto progresas: {}\n\n",
    "latest_commits.log": "📌 Naujausi commit'ai:\n",
    "important_tasks.json": "Automatinis užduočių sąrašas",
    "project_status.md": "📄 **Projekto būsena:**\n\n",
    "session_summary.txt": "📂 **Failų struktūra:**\n\n"
}

def ensure_directory():
    """Užtikrina, kad `gpt_help/` aplankas egzistuoja."""
    if not os.path.exists(GPT_HELP_DIR):
        os.makedirs(GPT_HELP_DIR)

def update_progress_summary():
    """Atnaujina progreso failą."""
    progress_file = os.path.join(GPT_HELP_DIR, "progress_summary.txt")
    with open(progress_file, "w", encoding="utf-8") as file:
        file.write(FILES["progress_summary.txt"].format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        file.write("- ✅ Naujos AI strategijos integracija\n")
        file.write("- ✅ Užduočių ir modelių valdymo sistema atnaujinta\n")
        file.write("- 🔜 Kitas žingsnis: Automatinė dokumentacijos generacija\n")

def update_latest_commits():
    """Sugeneruoja naujausių commit'ų failą ir užtikrina, kad jis būtų UTF-8 formato."""
    commits_file = os.path.join(GPT_HELP_DIR, "latest_commits.log")
    with open(commits_file, "w", encoding="utf-8") as file:
        file.write(FILES["latest_commits.log"])
        result = subprocess.run(["git", "log", "--oneline", "-n", "10"], capture_output=True, text=True, encoding="utf-8", errors="ignore")

        if result.stdout:  # ✅ Patikriname, ar yra commit'ų
            file.write(result.stdout)
        else:
            file.write("❌ Nepavyko gauti commit'ų istorijos.\n")


def update_important_tasks():
    """Sugeneruoja užduočių sąrašą JSON formatu."""
    tasks_file = os.path.join(GPT_HELP_DIR, "important_tasks.json")
    tasks = [
        {"title": "AI modelių optimizavimas", "status": "Vykdoma", "priority": "Aukštas"},
        {"title": "Strategijos generavimo tobulinimas", "status": "Baigta", "priority": "Vidutinis"},
        {"title": "Chat UI funkcionalumo plėtra", "status": "Vykdoma", "priority": "Aukštas"}
    ]
    with open(tasks_file, "w", encoding="utf-8") as file:
        json.dump({"tasks": tasks}, file, indent=4, ensure_ascii=False)

def update_project_status():
    """Atnaujina projekto būsenos failą."""
    status_file = os.path.join(GPT_HELP_DIR, "project_status.md")
    with open(status_file, "w", encoding="utf-8") as file:
        file.write(FILES["project_status.md"])
        file.write("## ✅ Baigti darbai:\n")
        file.write("- AI modelių valdymo sistema\n")
        file.write("- Užduočių registras ir strategijos generavimas\n")
        file.write("- Chat UI integracija su modelių perjungimu\n\n")
        file.write("## 🚀 Vykdomi darbai:\n")
        file.write("- AI instrukcijų analizė ir automatinis optimizavimas\n")
        file.write("- GPT pagalbos modulis projekto progresui įvertinti\n\n")
        file.write("## 🔜 Sekantys žingsniai:\n")
        file.write("- Testavimo automatizavimas\n")
        file.write("- Dokumentacijos generavimas realiu laiku\n")

def update_session_summary():
    """Sugeneruoja projekto failų struktūrą į session_summary.txt."""
    summary_file = os.path.join(GPT_HELP_DIR, "session_summary.txt")

    with open(summary_file, "w", encoding="utf-8") as file:
        file.write(FILES["session_summary.txt"])

    try:
        subprocess.run(["cmd.exe", "/c", "tree", "C:\\Users\\37065\\Projects\\ai.assist", "/A", "/F"], stdout=open(summary_file, "a", encoding="utf-8"), shell=True)
    except FileNotFoundError:
        with open(summary_file, "a", encoding="utf-8") as file:
            file.write("\n❌ Nepavyko sugeneruoti failų struktūros. Patikrinkite komandą `tree`.\n")


def generate_gpt_help():
    """Automatizuotas visų `gpt_help/` failų generavimas."""
    ensure_directory()
    update_progress_summary()
    update_latest_commits()
    update_important_tasks()
    update_project_status()
    update_session_summary()
    print(f"✅ Visi `gpt_help/` failai atnaujinti: {GPT_HELP_DIR}")

def generate_report():
    """Sugeneruoja bendrą sesijos ataskaitą viename faile."""
    with open(SESSION_REPORT, "w", encoding="utf-8") as report:
        report.write(f"🔹 **Session Report | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}**\n\n")
        
        for file in FILES.keys():
            file_path = os.path.join(GPT_HELP_DIR, file)
            if os.path.exists(file_path):
                report.write(f"📂 **{file}**\n")
                with open(file_path, "r", encoding="utf-8") as content:
                    report.write(content.read())
                report.write("\n" + "="*80 + "\n\n")
    
    print(f"✅ Sesijos ataskaita sukurta: {SESSION_REPORT}")

if __name__ == "__main__":
    generate_gpt_help()
    generate_report()
