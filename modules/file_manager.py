import os

def read_file(file_path):
    """Perskaito failo turinį ir grąžina kaip tekstą."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"🔴 Klaida: Failas '{file_path}' nerastas.")
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def write_file(file_path, content):
    """Įrašo turinį į failą. Jei failas neegzistuoja, jį sukuria."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

def file_exists(file_path):
    """Patikrina, ar failas egzistuoja."""
    return os.path.exists(file_path)

# Testavimas
if __name__ == "__main__":
    test_file = "test.txt"
    write_file(test_file, "Tai testinis failas.")
    print(f"📂 Failo '{test_file}' egzistavimas: {file_exists(test_file)}")
    print(f"📖 Failo turinys:\n{read_file(test_file)}")
