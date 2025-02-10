import unittest
import subprocess

class TestGitStatus(unittest.TestCase):
    """Testuoja Git būseną, ar nėra nepateiktų pakeitimų."""

    def run_git_command(self, command):
        """Vykdo Git komandą ir grąžina stdout bei stderr reikšmes."""
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip() if result.stdout else "", result.stderr.strip() if result.stderr else ""

    def test_git_status_clean(self):
        """Patikrina, ar nėra nepateiktų pakeitimų."""
        stdout, _ = self.run_git_command("git status --porcelain")
        self.assertEqual(stdout, "", "❌ Yra nepateiktų pakeitimų! Paleisk `git add .`, `git commit -m 'Tvarkinga būsena'` ir `git push`.")

    def test_git_branch_sync(self):
        """Patikrina, ar vietinė šaka yra sinchronizuota su GitHub."""
        result = self.run_git_command("git branch -vv")

        if result:
            stdout, _ = result
            stdout = stdout.strip()
        else:
            stdout = ""

        self.assertNotIn("[behind]", stdout, "❌ Vietinė Git šaka atsilieka nuo nuotolinės! Paleisk `git pull`.")

if __name__ == "__main__":
    unittest.main()
