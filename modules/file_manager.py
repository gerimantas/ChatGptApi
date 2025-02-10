# modules/file_manager.py

import os

class FileManager:
    """ Failų valdymo klasė, leidžianti skaityti, rašyti ir tikrinti failus. """

    @staticmethod
    def read_file(file_path: str) -> str:
        """Nuskaito ir grąžina failo turinį."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ Failas nerastas: {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def write_file(file_path: str, content: str) -> None:
        """Įrašo pateiktą tekstą į failą."""
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    @staticmethod
    def file_exists(file_path: str) -> bool:
        """Patikrina, ar failas egzistuoja."""
        return os.path.exists(file_path)

    @staticmethod
    def delete_file(file_path: str) -> None:
        """Ištrina nurodytą failą, jei jis egzistuoja."""
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"❌ Failas nerastas: {file_path}")

if __name__ == "__main__":
    # Testavimo pavyzdys
    test_path = "test_file.txt"
    FileManager.write_file(test_path, "Testinis turinys")
    print("📂 Sukurtas failas:", test_path)

    print("📖 Failo turinys:", FileManager.read_file(test_path))
    print("✅ Failas egzistuoja:", FileManager.file_exists(test_path))

    FileManager.delete_file(test_path)
    print("🗑️ Failas ištrintas:", not FileManager.file_exists(test_path))