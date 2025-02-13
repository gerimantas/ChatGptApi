import shutil
import os
import subprocess
import json

SOURCE_DIR = "Co/session_transfer/"
DEST_DIR = "Co/session_transfer/"
PROMPT_FILE = os.path.join(DEST_DIR, "chatgpt_prompt.txt")
STRUCTURE_FILE = os.path.join(DEST_DIR, "project_structure.txt")

def check_git_status():
    """Tikrina, ar visi pakeitimai yra `GitHub` repozitorijoje."""
    status_output = subprocess.getoutput("git status --porcelain")
    last_commit = subprocess.getoutput("git log -1 --oneline")

    if status_output:
        print("⚠️  Yra nepateiktų pakeitimų! Prieš perkeliant failus, commit'inkite ir push'inkite pakeitimus.")
        print("🛠️  Naudokite:")
        print("    git add .")
        print("    git commit -m 'Atnaujinta projekto būsena'")
        print("    git push origin main")
        return False
    
    print(f"✅ `GitHub` repozitorija sinchronizuota! Paskutinis commit'as: {last_commit}")
    return True

def prepare_transfer():
    """Užtikrina, kad visi CoinArbitr failai būtų `Co/session_transfer/` ir paruošia naują sesiją."""
    if not check_git_status():
        return

    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)

    for file_name in os.listdir(SOURCE_DIR):
        full_file_name = os.path.join(SOURCE_DIR, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, DEST_DIR)

    generate_chatgpt_prompt()
    generate_project_structure()
    print("✅ CoinArbitr failai sėkmingai paruošti ir **lieka** `Co/session_transfer/`!")

def generate_chatgpt_prompt():
    """Sugeneruoja `ChatGPT` promptą naujai CoinArbitr sesijai, išsaugant `Co/session_transfer/`."""
    context_data = {
        "session_summary": "Šioje sesijoje buvo atlikta pilna projekto failų struktūros optimizacija, visi `Co/session_transfer/` failai perkelti ir išsaugoti vietoje.",
        "critical_tasks": [
            "Užtikrinti, kad `Co/session_transfer/` būtų sinchronizuotas su `GitHub`.",
            "Užtikrinti, kad `pytest` testai veikia be klaidų.",
            "Pritaikyti papildomas funkcijas optimizuotoje struktūroje."
        ],
        "next_steps": [
            "Automatiškai atpažinti naują sesiją ir užtikrinti konteksto tęstinumą.",
            "Integruoti `ChatGPT` į naują sesiją su pilnu praėjusios sesijos kontekstu.",
            "Automatiškai inicijuoti CoinArbitr strategijos progresą naujoje sesijoje."
        ]
    }

    with open(PROMPT_FILE, "w") as f:
        json.dump(context_data, f, indent=4)

    print(f"✅ `ChatGPT` promptas naujai sesijai sugeneruotas į: {PROMPT_FILE}")

def generate_project_structure():
    """Sugeneruoja naują projekto failų struktūrą ir išsaugo `Co/session_transfer/`."""
    structure_data = subprocess.getoutput("tree /F /A")
    
    with open(STRUCTURE_FILE, "w", encoding="utf-8") as f:
        f.write(structure_data)

    print(f"✅ Atnaujinta projekto failų struktūra: {STRUCTURE_FILE}")

if __name__ == "__main__":
    prepare_transfer()
