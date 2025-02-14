import os
import shutil

# Sesijos failų keliai
SESSION_TRANSFER_DIR = "Co/session_transfer"
CURRENT_SESSION_DIR = "Co/current_session"
CHATGPT_PROMPT_FILE = os.path.join(SESSION_TRANSFER_DIR, "chatgpt_prompt.txt")
PROJECT_STRUCTURE_FILE = os.path.join(SESSION_TRANSFER_DIR, "project_structure.txt")
AI_INSTRUCTIONS_FILE = os.path.join(SESSION_TRANSFER_DIR, "ai_instructions.json")

# Sukuriame naują sesijos katalogą
os.makedirs(CURRENT_SESSION_DIR, exist_ok=True)

# Perkeliame reikiamus failus į naują sesiją
shutil.copy(PROJECT_STRUCTURE_FILE, os.path.join(CURRENT_SESSION_DIR, "project_structure.txt"))
shutil.copy(AI_INSTRUCTIONS_FILE, os.path.join(CURRENT_SESSION_DIR, "ai_instructions.json"))

# Informacija apie naują sesiją
print("✅ Nauja CoinArbitr sesija inicijuota!")
print(f"📄 Sesijos struktūra atnaujinta: {CURRENT_SESSION_DIR}/project_structure.txt")
print(f"📝 AI instrukcijos perkeltos: {CURRENT_SESSION_DIR}/ai_instructions.json")
print(f"💬 Naujos sesijos promptas: {CHATGPT_PROMPT_FILE}")

