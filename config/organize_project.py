import os
import shutil

# Nauja katalogų struktūra
DIRECTORIES = {
    "bot_aps": ["core", "ui", "logs", "tests", "config"],
    "Co": ["strategy", "session_transfer", "logs", "data", "scripts"]
}

# Atnaujintas failų sąrašas, pašalinti neegzistuojantys failai
FILES_TO_MOVE = {
    "bot_aps/core/openai_client.py": "bot_aps/core/",
    "bot_aps/core/api_usage_tracker.py": "bot_aps/core/",
    "bot_aps/core/task_manager.py": "bot_aps/core/",
    "bot_aps/core/file_manager.py": "bot_aps/core/",
    "bot_aps/core/doc_generator.py": "bot_aps/core/",
    "bot_aps/core/config.py": "bot_aps/core/",
    "bot_aps/ui/assistant_ui.py": "bot_aps/ui/",
    "bot_aps/ui/chat_ui.py": "bot_aps/ui/",
    "bot_aps/ui/ui_config.py": "bot_aps/ui/",
    "Co/strategy/co_strategy.json": "Co/strategy/",
    "Co/strategy/co_strategy_info.json": "Co/strategy/",
    "Co/strategy/progress_tracking.json": "Co/strategy/",
    "Co/strategy/strategy_tracker.py": "Co/strategy/"
}

def create_directories():
    """Sukuria trūkstamus katalogus."""
    for parent, subdirs in DIRECTORIES.items():
        os.makedirs(parent, exist_ok=True)
        for subdir in subdirs:
            os.makedirs(os.path.join(parent, subdir), exist_ok=True)

def move_files():
    """Perkelia failus į naują struktūrą."""
    for source, target in FILES_TO_MOVE.items():
        if os.path.exists(source):
            os.makedirs(target, exist_ok=True)
            shutil.move(source, os.path.join(target, os.path.basename(source)))
            print(f"✅ Perkelta: {source} → {target}")
        else:
            print(f"⚠️ Įspėjimas: {source} nerastas. Perkėlimas praleistas.")

if __name__ == "__main__":
    print("🚀 Pradedamas projekto pertvarkymas...")
    create_directories()
    move_files()
    print("✅ Projekto pertvarkymas baigtas!")
