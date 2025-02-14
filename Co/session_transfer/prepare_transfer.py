import shutil
import os
import subprocess
import json

SOURCE_DIR = "Co/"
DEST_DIR = "Co/session_transfer/"
PROMPT_FILE = os.path.join(DEST_DIR, "chatgpt_prompt.txt")
STRUCTURE_FILE = os.path.join(DEST_DIR, "project_structure.txt")

def check_git_status():
    """Checks if there are any uncommitted changes in the Git repository."""
    status_output = subprocess.getoutput("git status --porcelain")
    last_commit = subprocess.getoutput("git log -1 --oneline")

    if status_output:
        print("⚠️  Uncommitted changes detected! Please commit and push before proceeding.")
        print("🛠️  Use the following commands:")
        print("    git add .")
        print("    git commit -m 'Updated project state'")
        print("    git push origin main")
        return False
    
    print(f"✅ GitHub repository is synchronized! Last commit: {last_commit}")
    return True

def prepare_transfer():
    """Copies CoinArbitr session files to the `Co/session_transfer/` directory if Git is clean."""
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
    print("✅ CoinArbitr files are prepared for session transfer!")

def generate_chatgpt_prompt():
    """Generates the ChatGPT session prompt and saves it in `Co/session_transfer/`."""
    context_data = {
        "session_summary": "During this session, the project file structure was fully optimized, and files were reorganized in `Co/session_transfer/`.",
        "critical_tasks": [
            "Ensure that `Co/session_transfer/` files are properly prepared for the next session.",
            "Verify that `pytest` tests run without errors.",
            "Synchronize `GitHub` with the new session updates.",
            "Apply additional optimizations in the improved structure."
        ],
        "next_steps": [
            "Automatically detect the new session and ensure context continuity.",
            "Integrate `ChatGPT` into the new session with full previous session context.",
            "Automatically initiate CoinArbitr strategy progress tracking in the new session."
        ]
    }

    with open(PROMPT_FILE, "w") as f:
        json.dump(context_data, f, indent=4)

    print(f"✅ ChatGPT session prompt generated: {PROMPT_FILE}")

def generate_project_structure():
    """Generates an updated project file structure and saves it in `Co/session_transfer/`."""
    structure_data = subprocess.getoutput("tree /F /A")
    
    with open(STRUCTURE_FILE, "w", encoding="utf-8") as f:
        f.write(structure_data)

    print(f"✅ Updated project file structure saved: {STRUCTURE_FILE}")

if __name__ == "__main__":
    prepare_transfer()
