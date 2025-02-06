import openai
import os
import dotenv

# Įkeliame API raktą iš .env failo
dotenv.load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Patikriname, ar API raktas yra nustatytas
if not api_key:
    raise ValueError("🔴 API raktas nerastas! Patikrink .env failą.")

# Nauja OpenAI API sąsaja
client = openai.OpenAI(api_key=api_key)

# Funkcija siųsti užklausas į OpenAI API
def send_message_to_gpt(messages, model="gpt-4-turbo", max_tokens=1000):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except openai.OpenAIError as e:
        return f"🔴 API klaida: {str(e)}"

# Funkcija, skirta AI logams fiksuoti
def log_interaction(user_input, ai_response, log_file="ai_logs.txt"):
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"\n👤 Vartotojas: {user_input}\n🤖 AI: {ai_response}\n")

# Testavimas
if __name__ == "__main__":
    test_messages = [{"role": "user", "content": "Labas, kaip tau sekasi?"}]
    ai_response = send_message_to_gpt(test_messages)
    log_interaction(test_messages[0]["content"], ai_response)
    print(f"🤖 AI atsakymas: {ai_response}")
