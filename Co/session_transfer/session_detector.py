import json
import os
import shutil
import uuid
import csv
import subprocess
from datetime import datetime, timezone

SESSION_TRANSFER_DIR = "Co/session_transfer/"
SESSION_SUMMARY_FILE = os.path.join(SESSION_TRANSFER_DIR, "session_summary.json")
AI_INSTRUCTIONS_FILE = "Co/ai_instructions.json"
STRATEGY_FILES = ["Co/strategy.json", "Co/progress_tracking.json"]
PREVIOUS_PROGRESS_FILE = "Co/previous_progress_tracking.json"
SESSION_ID_FILE = "Co/session_id.json"
SESSION_HISTORY_FILE = "Co/session_history.json"
SESSION_TASKS_FILE = "Co/session_tasks.json"
SESSION_MESSAGE_COUNT_FILE = os.path.join(SESSION_TRANSFER_DIR, "session_message_count.json")
CHATGPT_PROMPT_FILE = os.path.join(SESSION_TRANSFER_DIR, "chatgpt_prompt.txt")
SESSION_DETECTOR_FILE = os.path.join(SESSION_TRANSFER_DIR, "session_detector.json")

prompt_triggered = False  # Global flag to avoid double detection


def ensure_file_structure():
    """Ensures that all necessary files exist and are in the correct directories."""
    file_defaults = {
        SESSION_MESSAGE_COUNT_FILE: {"message_count": 0},
        SESSION_DETECTOR_FILE: {"session_id": "", "timestamp": "", "message_count": 0},
        SESSION_ID_FILE: {"session_id": "", "timestamp": ""},
        SESSION_HISTORY_FILE: [],
        SESSION_TASKS_FILE: {}
    }
    
    for file, default_content in file_defaults.items():
        if not os.path.exists(file):
            with open(file, "w", encoding="utf-8") as f:
                json.dump(default_content, f, indent=4)
            print(f"📂 Created missing file: {file}")


def save_session_history(session_data):
    """Stores session history for future reference."""
    history = []
    if os.path.exists(SESSION_HISTORY_FILE):
        with open(SESSION_HISTORY_FILE, "r", encoding="utf-8") as file:
            history = json.load(file)
    history.append(session_data)
    with open(SESSION_HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)
    print("📌 Session history updated.")


def save_session_detector(session_data):
    """Stores session detection parameters for next session recognition."""
    with open(SESSION_DETECTOR_FILE, "w", encoding="utf-8") as file:
        json.dump(session_data, file, indent=4)
    print("📌 Session detector updated.")


def get_real_message_count():
    """Attempts to restore the correct message count by checking the session file."""
    if os.path.exists(SESSION_MESSAGE_COUNT_FILE):
        with open(SESSION_MESSAGE_COUNT_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data.get("message_count", 0)
    return 0


def update_message_count(reset=False):
    """Increments or resets the message count for the session and warns if nearing limit."""
    message_count = 1 if reset else get_real_message_count() + 1
    
    if message_count >= 100:
        print("⚠️ WARNING: Session has reached 100 messages. Consider starting a new session.")
    
    with open(SESSION_MESSAGE_COUNT_FILE, "w", encoding="utf-8") as file:
        json.dump({"message_count": message_count}, file, indent=4)
    
    print(f"🔢 Session Message Count Updated: {message_count}")


def detect_prompt_trigger():
    """Checks if a new session is initiated using chatgpt_prompt.txt."""
    global prompt_triggered
    if os.path.exists(CHATGPT_PROMPT_FILE) and not prompt_triggered:
        prompt_triggered = True
        print("📥 Detected chatgpt_prompt.txt - Starting new session from #1")
        return True
    return False


def generate_session_id():
    """Generates a unique session identifier and stores it."""
    session_id = str(uuid.uuid4())
    session_data = {
        "session_id": session_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "message_count": 1 if prompt_triggered else get_real_message_count()
    }
    with open(SESSION_ID_FILE, "w", encoding="utf-8") as file:
        json.dump(session_data, file, indent=4)
    save_session_history(session_data)
    save_session_detector(session_data)
    return session_id


def detect_new_session():
    """Detects if a new session has started by checking for session summary file and session detector."""
    global prompt_triggered
    prompt_triggered = detect_prompt_trigger()
    
    if prompt_triggered:
        print("🔄 Starting new session from #1")
        session_id = generate_session_id()
        update_message_count(reset=True)
        return {"session_id": session_id}
    
    if os.path.exists(SESSION_DETECTOR_FILE):
        with open(SESSION_DETECTOR_FILE, "r", encoding="utf-8") as file:
            session_data = json.load(file)
        print(f"🛠 Restoring session from session detector (ID: {session_data.get('session_id', 'N/A')})")
        update_message_count()
        return session_data
    
    if os.path.exists(SESSION_SUMMARY_FILE):
        with open(SESSION_SUMMARY_FILE, "r", encoding="utf-8") as file:
            session_data = json.load(file)
        print(f"✅ Previous session detected (ID: {session_data.get('session_id', 'N/A')}). Restoring context...")
        update_message_count()
        return session_data
    else:
        print("⚠️ No previous session found. Starting a new session.")
        session_id = generate_session_id()
        print(f"🆔 New Session ID: {session_id}")
        return {"session_id": session_id}


if __name__ == "__main__":
    ensure_file_structure()
    session_data = detect_new_session()
    update_message_count()
    print("🚀 Session setup complete!")
