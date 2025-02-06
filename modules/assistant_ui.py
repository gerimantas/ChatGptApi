import openai
import os
import dotenv
import colorama
from colorama import Fore, Style
from modules.openai_client import send_message_to_gpt

# Įkeliame API raktą iš .env failo
dotenv.load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("🔴 API raktas nerastas! Patikrink .env failą.")

# Inicializuojame spalvų biblioteką
colorama.init()

# Funkcija pokalbio su AI vykdymui
def start_chat():
    """Interaktyvus pokalbio režimas terminale su režimų pasirinkimu."""
    print(Fore.CYAN + "🤖 AI Asistentas aktyvus!" + Style.RESET_ALL)
    print("🔹 Pasirink režimą: ")
    print("   1️⃣ Kodo generavimas")
    print("   2️⃣ Kodo optimizavimas")
    print("   3️⃣ Klaidų taisymas")
    print("   4️⃣ Laisvas pokalbis")
    mode = input(Fore.YELLOW + "✏️ Įvesk pasirinkimą (1-4): " + Style.RESET_ALL)

    mode_mapping = {
        "1": "Kodo generavimas",
        "2": "Kodo optimizavimas",
        "3": "Klaidų taisymas",
        "4": "Laisvas pokalbis"
    }
    
    selected_mode = mode_mapping.get(mode, "Laisvas pokalbis")
    print(Fore.GREEN + f"✅ Pasirinktas režimas: {selected_mode}" + Style.RESET_ALL)

    while True:
        user_input = input(Fore.YELLOW + "👤 Tu: " + Style.RESET_ALL)

        if user_input.lower() == "exit":
            print(Fore.RED + "👋 Pokalbis baigtas." + Style.RESET_ALL)
            break

        messages = [
            {"role": "system", "content": f"Tu esi AI asistentas, kuris padeda su {selected_mode}."},
            {"role": "user", "content": user_input}
        ]

        ai_response = send_message_to_gpt(messages)

        log_chat(user_input, ai_response)

        print(Fore.CYAN + f"🤖 AI: {ai_response}" + Style.RESET_ALL)

# Funkcija pokalbio išsaugojimui logų faile
def log_chat(user_input, ai_response, log_file="chat_logs.txt"):
    """Išsaugo vartotojo ir AI pokalbį faile."""
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"\n👤 Vartotojas: {user_input}\n🤖 AI: {ai_response}\n")

# Jei paleidžiamas kaip pagrindinis failas, pradedame pokalbį
if __name__ == "__main__":
    start_chat()
