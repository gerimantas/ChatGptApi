import openai
import os
import json
import speech_recognition as sr
from gtts import gTTS
from dotenv import load_dotenv

# Įkeliame API raktą iš .env failo
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Patikriname, ar API raktas įkeltas
if not api_key:
    raise ValueError("🔴 API raktas nerastas! Patikrink .env failą.")

# Sukuriame OpenAI klientą
client = openai.OpenAI(api_key=api_key)

# Failo pavadinimas pokalbio istorijai išsaugoti
HISTORY_FILE = "chat_history.json"

# Įkeliame pokalbio istoriją iš failo
def load_conversation_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return [{"role": "system", "content": "Tu esi naudingas ir draugiškas asistentas."}]

# Išsaugome pokalbio istoriją į failą
def save_conversation_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

# Funkcija, leidžianti atkurti tekstą balsu su Google TTS
def speak(text):
    tts = gTTS(text=text, lang="lt")
    tts.save("response.mp3")
    os.system("start response.mp3")

# Funkcija, leidžianti klausytis mikrofono su timeout apsauga
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Kalbėkite į mikrofoną... (arba laukite, jei norite išeiti iš balso režimo)")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Prisitaiko prie foninio triukšmo
        try:
            audio = recognizer.listen(source, timeout=5)  # Jei nieko nesakoma, laukiama 5 sek.
            print("🔊 Atpažįstu garsą...")
            return recognizer.recognize_google(audio, language="lt-LT")  # Atpažįsta lietuvių kalbą
        except sr.WaitTimeoutError:
            print("⏳ Laikas baigėsi. Grįžtama į tekstinį režimą.")
            return None
        except sr.UnknownValueError:
            print("❌ Nepavyko suprasti jūsų balso. Perjungiu į tekstinį režimą.")
            return None
        except sr.RequestError as e:
            print(f"❌ Balso atpažinimo paslaugos klaida: {e}")
            return None

# Pokalbio istorija
conversation_history = load_conversation_history()

def chatbot():
    print("🤖 Chatbotas aktyvus!")
    print("✅ Komandos: 'k' - kalbėti, 'b' - atsakyti balsu, 'r' - atsakyti raštu, 'e' - baigti pokalbį.")
    use_voice_input = False  # Ar vartotojas naudoja balsą įvedimui?
    use_voice_output = False  # Ar chatbotas atsako balsu?

    while True:
        if use_voice_input:
            user_input = listen()
            if user_input:
                print(f"👤 Atpažinta balso žinutė: {user_input}")  # Rodo atpažintą tekstą
            else:
                use_voice_input = False  # Jei nepavyko suprasti arba laikas baigėsi, grįžtame į tekstinį režimą
                continue
        else:
            user_input = input("👤 Tu: ")

        if user_input.lower() == "e":
            print("👋 Iki pasimatymo!")
            break
        elif user_input.lower() == "k":
            print("🎤 Perjungta į balso režimą. Dabar galite tiesiog kalbėti.")
            use_voice_input = True
            continue
        elif user_input.lower() == "b":
            print("🔊 Chatbotas atsakinės balsu.")
            use_voice_output = True
            continue
        elif user_input.lower() == "r":
            print("✍️ Chatbotas atsakinės raštu.")
            use_voice_output = False
            continue

        if user_input:
            # Pridedame vartotojo žinutę į istoriją
            conversation_history.append({"role": "user", "content": user_input})

            # Siunčiame užklausą OpenAI API
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=conversation_history
            )
            print(f"🔍 Naudojamas GPT modelis: {response.model}")  # Atspausdina modelio versijąKokia

            # Išsaugome atsakymą istorijoje
            bot_response = response.choices[0].message.content
            conversation_history.append({"role": "assistant", "content": bot_response})
            save_conversation_history(conversation_history)

            # Atsakome vartotojui vienu pasirinktu būdu
            print("🤖 Chatbotas:", bot_response)
            if use_voice_output:
                speak(bot_response)  # Jei balsas aktyvus, chatbotas atsako garsiai

# Paleidžiame chatbotą
if __name__ == "__main__":
    chatbot()

