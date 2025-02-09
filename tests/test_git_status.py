import subprocess
import unittest

class TestGitStatus(unittest.TestCase):
    def run_git_command(self, command):
        """Paleidžia Git komandą ir grąžina išvestį su UTF-8 kodavimu."""
        result = subprocess.run(command, shell=True, text=True, capture_output=True, encoding="utf-8")
        stdout = result.stdout.strip() if result.stdout else ""
        stderr = result.stderr.strip() if result.stderr else ""
        return stdout, stderr

    def test_git_status_clean(self):
        """Patikrina, ar nėra nepateiktų pakeitimų."""
        stdout, stderr = self.run_git_command("git status --porcelain")
        self.assertEqual(stdout, "", "❌ Yra nepateiktų pakeitimų! Paleisk `git status`, tada `git add .` ir `git commit -m 'Tvarkinga būsena'`.")

    def test_git_remote_configured(self):
        """Patikrina, ar nuotolinė saugykla (`origin`) yra sukonfigūruota."""
        stdout, stderr = self.run_git_command("git remote -v")
        self.assertIn("origin", stdout, "❌ Nuotolinė saugykla nėra nustatyta! Paleisk `git remote -v`.")

    def test_git_can_fetch(self):
        """Patikrina, ar galima prisijungti prie GitHub ir atnaujinti informaciją."""
        stdout, stderr = self.run_git_command("git fetch origin")
        self.assertEqual(stderr, "", "❌ Nepavyko atnaujinti informacijos iš GitHub! Paleisk `git fetch origin`.")

    def test_git_branch_sync(self):
        """Patikrina, ar vietinė šaka yra sinchronizuota su GitHub."""
        stdout, stderr = self.run_git_command("git branch -vv")
        self.assertIn("[origin/", stdout, "❌ Vietinė šaka nesinchronizuota su nuotoline! Paleisk `git branch -vv`, tada `git pull origin main`.")

if __name__ == "__main__":
    unittest.main()
