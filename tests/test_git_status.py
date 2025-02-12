import unittest
import subprocess

class TestGitStatus(unittest.TestCase):
    """Testuoja Git būseną, ar nėra nepateiktų pakeitimų (išskyrus `cache/`)."""

    def run_git_command(self, command):
        """Vykdo Git komandą ir grąžina stdout bei stderr reikšmes, naudodamas UTF-8 koduotę."""
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8", errors="ignore")
        return result.stdout.strip() if result.stdout else "", result.stderr.strip() if result.stderr else ""

    # 🔹 Copilot: Optimizuok šią funkciją, kad ji neblokuotų commit'ų, jei `tests/test_git_status.py` yra aktyviai redaguojamas.
    def test_git_status_clean(self):
        """Patikrina, ar nėra nepateiktų pakeitimų (išskyrus `cache/`)."""
        stdout, _ = self.run_git_command("git status --porcelain")

        # ✅ Ignoruojami failai ir aplankai
        ignored_changes = [
            "cache/",
            "cache/openai_cache.db",
            ".gitignore",
            "*.log",
            "__pycache__/",
            ".DS_Store",
            ".vscode/",
            "tests/test_git_status.py"  # Pridedame save į ignoruojamus failus
        ]

        # ✅ Tikriname, ar failai yra `staged`
        staged_files, _ = self.run_git_command("git diff --cached --name-only")
        staged_files = staged_files.split("\n") if staged_files else []

        # ✅ Filtruojame nepateiktus pakeitimus, atmesdami ignoruojamus ir jau `staged` failus
        filtered_stdout = "\n".join(
            line for line in stdout.split("\n")
            if line and not any(ignored in line for ignored in ignored_changes)  
            and not any(staged_file in line for staged_file in staged_files)  # ✅ Pataisyta kintamojo klaida
        )

        self.assertEqual(
            filtered_stdout, "", 
            "❌ Yra nepateiktų pakeitimų! Paleisk `git add .`, `git commit -m 'Tvarkinga būsena'` ir `git push`."
        )

    def test_git_branch_sync(self):
        """Patikrina, ar vietinė šaka yra sinchronizuota su GitHub."""
        stdout, _ = self.run_git_command("git branch -vv")

        if stdout:
            stdout = stdout.strip()

        self.assertNotIn("[behind]", stdout, "❌ Vietinė Git šaka atsilieka nuo nuotolinės! Paleisk `git pull`.")
        self.assertNotIn("[ahead]", stdout, "❌ Vietinė Git šaka yra priekyje! Paleisk `git push`.")

    # 🔹 Copilot: Optimizuok šią funkciją, kad ji neblokuotų commit'ų, jei `tests/test_git_status.py` yra aktyviai redaguojamas.
    def test_git_diff_clean(self):
        """Patikrina, ar nėra necommit'intų pakeitimų (`git diff --name-only`)."""
        stdout, _ = self.run_git_command("git diff --name-only")

        # ✅ Jei vienintelis pakeitimas yra `tests/test_git_status.py`, jis ignoruojamas
        filtered_stdout = "\n".join(
            line for line in stdout.split("\n") if line and line != "tests/test_git_status.py"
        )

        self.assertEqual(
            filtered_stdout, "", 
            "❌ Yra necommit'intų pakeitimų! Paleisk `git add .`, `git commit -m 'Tvarkinga būsena'` ir `git push`."
        )

if __name__ == "__main__":
    unittest.main()
