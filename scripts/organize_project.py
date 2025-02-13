import os
import shutil

# Apibrėžiame naują katalogų struktūrą
DIRECTORIES = {
    "Co": ["Co_strategy", "session_transfer"],
    "config": [],
    "scripts": [],
    "data": [],
    "modules/core": [],
    "modules/ui": [],
    "modules/logs": [],
    "modules/tests": ["logs"],
}

FILES_TO_MOVE = {
    "ai_instructions.json": "Co/session_transfer/",
    "session_context.txt": "Co/session_transfer/",
    "ai_assist_tree.txt": "Co/session_transfer/",
    "project_structure.txt": "Co/session_transfer/",
    "progress_tracking.json": "Co/Co_strategy/",
    "strategy_tracker.py": "Co/Co_strategy/",
    "co_strategy.json": "Co/Co_strategy/",
    "co_strategy_info.json": "Co/Co_strategy/",
    "config.json": "config/",
    "pytest.ini": "config/",
    ".env": "config/",
    "ui_config.py": "config/",
    "scan_project_structure.py": "scripts/",
    "fill_strategy.py": "scripts/",
    "generate_session_report.ps1": "scripts/",
    "check_gpt_model.py": "scripts/",
    "test_script.py": "scripts/",
    "chat_history.json": "data/",
    "backlog.txt": "data/",
    "project_plan.md": "data/",
    "file_hashes.txt": "data/",
    "openai_cache.db": "data/",
    "openai_client.py": "modules/core/",
    "file_manager.py": "modules/core/",
    "api_usage_tracker.py": "modules/core/",
    "config.py": "modules/core/",
    "task_manager.py": "modules/core/",
    "doc_generator.py": "modules/core/",
    "assistant_ui.py": "modules/ui/",
    "chat_ui.py": "modules/ui/",
    "openai_client.log": "modules/logs/",
    "openai_client_errors.log": "modules/logs/",
}

IGNORE_PATTERNS = [".git", "__pycache__", "*.log", "cache/"]

def create_directories():
    """Sukuria trūkstamus katalogus."""
    for parent, subdirs in DIRECTORIES.items():
        os.makedirs(parent, exist_ok=True)
        for subdir in subdirs:
            os.makedirs(os.path.join(parent, subdir), exist_ok=True)

def move_files():
    """Perkelia failus į naują struktūrą."""
    for file, target_dir in FILES_TO_MOVE.items():
        if os.path.exists(file):
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(file, os.path.join(target_dir, file))
            print(f"✅ Perkelta: {file} → {target_dir}")

def cleanup():
    """Pašalina tuščius aplankus ir nereikalingus failus."""
    for root, dirs, files in os.walk(".", topdown=False):
        for name in dirs:
            dir_path = os.path.join(root, name)
            if not os.listdir(dir_path) and name not in DIRECTORIES.keys():
                os.rmdir(dir_path)
                print(f"🗑️ Ištrintas tuščias aplankas: {dir_path}")

if __name__ == "__main__":
    print("🚀 Pradedamas projekto pertvarkymas...")
    create_directories()
    move_files()
    cleanup()
    print("✅ Projekto pertvarkymas baigtas!")
