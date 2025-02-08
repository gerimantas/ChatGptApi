import openai
import os
from dotenv import load_dotenv

# Įkeliame API raktą iš .env failo
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Sukuriame OpenAI klientą
client = openai.OpenAI(api_key=api_key)

# Atliekame testinę užklausą
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Koks modelis dabar naudojamas?"}]
)

print(f"🔍 Naudojamas GPT modelis: {response.model}")
