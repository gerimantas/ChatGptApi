import os
import shutil
import subprocess

# Perkėlimo žemėlapis (senas kelias → naujas kelias)
migration_map = {
    "ai_core/instruction_loader.py": "APS_strategy/objective_definer.py",
    "ai_core/model_selection.py": "APS_model_selection/model_selector.py",
    "ai_core/task_analysis.py": "APS_strategy/strategy_analyzer.py",
    "ai_core/task_execution.py": "APS_project_manager/project_tracker.py",
    "ai_core/versioning.py": "APS_management/system_monitor.py",
    "ai_core/workspace_setup.py": "APS_structure/structure_optimizer.py",
    "automation/automation.py": "APS_management/logs_handler.py",
    "error_tracking/error_tracking.py": "APS_management/security_manager.py",
    "file_management/file_management.py": "APS_structure/structure_logger.py",
    "config.json": "config/config.json",
    ".env": "config/.env"
}

def move_files():
    """Perkelia failus pagal naują struktūrą naudojant `git mv`, išvengiant konfliktų."""
    for old_path, new_path in migration_map.items():
        if os.path.exists(old_path):
            os.makedirs(os.path.dirname(new_path), exist_ok=True)

            # Jei tikslinis failas jau egzistuoja, sukuria atsarginę kopiją
            if os.path.exists(new_path):
                backup_path = new_path + ".backup"
                shutil.move(new_path, backup_path)
                print(f"⚠️ Atsarginė kopija sukurta: {backup_path}")

            subprocess.run(["git", "mv", old_path, new_path], check=True)
            print(f"✅ Perkeltas: {old_path} → {new_path}")

def update_imports():
    """Atnaujina import kelius visose Python bylose."""
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Pakeičiame senus importus naujais
                for old_path, new_path in migration_map.items():
                    old_module = old_path.replace("/", ".").replace(".py", "")
                    new_module = new_path.replace("/", ".").replace(".py", "")
                    content = content.replace(f"from {old_module}", f"from {new_module}")

                # Išsaugome pakeitimus
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"🔄 Atnaujinti importai: {file_path}")

def run_tests():
    """Paleidžia `pytest`, kad patikrintų, ar viskas veikia po perkėlimo."""
    print("🚀 Paleidžiami testai...")
    subprocess.run(["pytest"], check=False)

def commit_changes():
    """Sukuria Git commit su migracijos pranešimu."""
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "🔄 Failų struktūros migracija pagal Aivolt modelį"], check=True)
    print("✅ Git commit sėkmingai sukurtas.")

if __name__ == "__main__":
    print("🚀 Pradedamas failų perkėlimas pagal Aivolt modelį...")
    move_files()
    update_imports()
    run_tests()
    commit_changes()
    print("🎉 Migracija sėkmingai baigta!")
