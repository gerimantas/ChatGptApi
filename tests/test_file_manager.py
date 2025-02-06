import sys
import os

# Pridedame projekto šaknies aplanką į Python kelių sąrašą
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.file_manager import read_file, write_file, file_exists

# Testinis failo pavadinimas
test_file = "test_file.txt"

# Testas: Įrašyti ir perskaityti failą
write_file(test_file, "Testinis failo turinys.")
assert file_exists(test_file) == True, "❌ Klaida: Failas turėjo egzistuoti, bet nebuvo rastas."
assert read_file(test_file) == "Testinis failo turinys.", "❌ Klaida: Netikslus failo turinys."

print("✅ Visi failų sistemos testai sėkmingai praėjo!")
