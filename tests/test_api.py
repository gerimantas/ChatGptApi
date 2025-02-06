import sys
import os

# Pridedame projekto šaknies aplanką į Python kelių sąrašą
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.openai_client import send_message_to_gpt

# Testinė žinutė AI modeliui
test_messages = [{"role": "user", "content": "Labas, kaip tau sekasi?"}]

# Vykdoma užklausa į OpenAI API
ai_response = send_message_to_gpt(test_messages)

# Rezultato atvaizdavimas terminale
print(f"🤖 AI atsakymas: {ai_response}")
