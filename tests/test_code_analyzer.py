import sys
import os

# Pridedame projekto šaknies aplanką į Python kelių sąrašą
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.code_analyzer import analyze_code

# Sukuriame testinį Python failą
test_file = "test_script.py"
with open(test_file, "w") as f:
    f.write("print('Hello World')\nfor i in range(len([1,2,3])): print(i)")

# Atliekame analizę
result = analyze_code(test_file)

# Testuojame klaidų aptikimą
assert isinstance(result["issues"], list), "❌ Klaida: `issues` turėtų būti sąrašas."
assert isinstance(result["optimizations"], list), "❌ Klaida: `optimizations` turėtų būti sąrašas."

print("🔍 Aptiktos problemos:", result["issues"])
print("✨ Optimizacijos pasiūlymai:", result["optimizations"])
print("✅ Visi kodo analizės testai sėkmingai praėjo!")
