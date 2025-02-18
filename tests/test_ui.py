import sys
import os

# Pridedame projekto šaknies aplanką į Python kelių sąrašą
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from APS_project_manager.AI_assistant.assistant_ui import start_chat

# Testavimas
if __name__ == "__main__":
    print("🔍 Testuojamas AI UI sąsajos paleidimas...")
    start_chat()
1

