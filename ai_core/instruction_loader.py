import json
import os
from typing import List, Dict

INSTRUCTION_DIR = "config"
INSTRUCTION_FILE = os.path.join(INSTRUCTION_DIR, "ai_instructions.json")

def ensure_instruction_directory():
    """Patikrina, ar egzistuoja instrukcijų aplankas, jei ne – sukuria jį."""
    if not os.path.exists(INSTRUCTION_DIR):
        os.makedirs(INSTRUCTION_DIR)
        print(f"📁 Sukurtas aplankas: {INSTRUCTION_DIR}")

def load_instructions() -> Dict:
    """Įkelia AI instrukcijas iš JSON failo."""
    ensure_instruction_directory()
    if not os.path.exists(INSTRUCTION_FILE):
        raise FileNotFoundError(f"Instrukcijų failas nerastas: {INSTRUCTION_FILE}")
    
    with open(INSTRUCTION_FILE, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            validate_instructions(data)
            return data
        except json.JSONDecodeError:
            raise ValueError("Instrukcijų failas yra netinkamo formato.")

def validate_instructions(data: Dict):
    """Patikrina, ar instrukcijų failas turi reikiamus laukus."""
    required_keys = ["AI_INSTRUCTIONS_VERSION", "LAST_UPDATED", "WORK_ENVIRONMENT", "MODEL_SELECTION", "API_CONFIGURATION"]
    
    for key in required_keys:
        if key not in data:
            raise KeyError(f"Trūksta būtino instrukcijų rakto: {key}")

def update_instructions(new_data: Dict):
    """Atnaujina AI instrukcijas su naujais duomenimis."""
    ensure_instruction_directory()
    validate_instructions(new_data)
    
    with open(INSTRUCTION_FILE, "w", encoding="utf-8") as file:
        json.dump(new_data, file, indent=4, ensure_ascii=False)
    print("✅ AI instrukcijos atnaujintos!")

def switch_model(new_model: str):
    """Keičia naudojamą AI modelį, jei jis egzistuoja instrukcijų faile."""
    instructions = load_instructions()
    available_models = instructions.get("MODEL_SELECTION", {}).get("AVAILABLE_MODELS", [])
    
    if new_model not in available_models:
        raise ValueError(f"Modelis '{new_model}' nėra prieinamas. Galimi modeliai: {available_models}")
    
    instructions["MODEL_SELECTION"]["DEFAULT_MODEL"] = new_model
    update_instructions(instructions)
    print(f"🔄 AI modelis pakeistas į: {new_model}")

def get_api_storage_location() -> str:
    """Grąžina API raktų saugojimo vietą iš instrukcijų."""
    instructions = load_instructions()
    return instructions.get("API_CONFIGURATION", {}).get("API_KEY_STORAGE", "Nenurodyta")

def test_instruction_loader():
    """Paprastas testas, patikrinantis funkcijų veikimą."""
    try:
        print("🔍 Tikriname instrukcijų aplanko egzistavimą...")
        ensure_instruction_directory()
        print("✅ Instrukcijų aplankas egzistuoja arba buvo sukurtas!")
        
        print("🔍 Tikriname instrukcijų įkėlimą...")
        instructions = load_instructions()
        print("✅ Instrukcijos sėkmingai įkeltos!")
        
        print("🔍 Tikriname modelių instrukcijų adaptavimą...")
        switch_model("gpt-4o")
        print("✅ Modelio pakeitimas sėkmingas!")
        
        print("🔍 Tikriname API raktų saugojimo vietą...")
        api_storage = get_api_storage_location()
        print(f"✅ API raktų saugojimo vieta: {api_storage}")
        
    except Exception as e:
        print(f"❌ Testas nepavyko: {e}")

if __name__ == "__main__":
    test_instruction_loader()
