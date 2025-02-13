import shutil
import os
import subprocess
import json

SOURCE_DIR = "Co/"
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
    """Kopijuoja CoinArbitr failus į kitą sesiją tik jei `GitHub` yra sinchronizuotas."""
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
    print("✅ CoinArbitr failai paruošti perkėlimui į kitą sesiją!")

def generate_chatgpt_prompt():
    """Sugeneruoja `ChatGPT` promptą naujai CoinArbitr sesijai."""
    context_data = {
        "session_summary": "Šioje sesijoje buvo atlikta pilna projekto failų struktūros optimizacija, sukurti ir pertvarkyti `next_session/` aplanko failai.",
        "critical_tasks": [
            "Perkelti `next_session/` failus į naują sesiją.",
            "Užtikrinti, kad `pytest` testai veikia be klaidų.",
            "Sinchronizuoti `GitHub` su naujos sesijos pokyčiais.",
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

    print(f"✅ `ChatGPT` promptas naujai sesijai sugeneruotas: {PROMPT_FILE}")

def generate_project_structure():
    """Sugeneruoja naują projekto failų struktūrą."""
    structure_data = subprocess.getoutput("tree /F /A")
    
    with open(STRUCTURE_FILE, "w", encoding="utf-8") as f:
        f.write(structure_data)

    print(f"✅ Atnaujinta projekto failų struktūra: {STRUCTURE_FILE}")

if __name__ == "__main__":
    prepare_transfer()
