import unittest
import subprocess

class TestGitStatus(unittest.TestCase):
    def run_git_command(self, command):
        """Vykdo Git komandą ir grąžina jos išvestį."""
        result = subprocess.run(command.split(), capture_output=True, text=True)
        return result.stdout.strip(), result.stderr.strip()

    def test_git_status_clean(self):
        """Patikrina, ar nėra nepateiktų pakeitimų."""
        stdout, _ = self.run_git_command("git status --porcelain")
        self.assertEqual(stdout, "", "❌ Yra nepateiktų pakeitimų! Paleisk `git add .`, `git commit -m 'Tvarkinga būsena'` ir `git push`.")

    def test_git_branch_sync(self):
        """Patikrina, ar vietinė šaka yra sinchronizuota su GitHub."""
        stdout, _ = self.run_git_command("git branch -vv")
        self.assertIn("[origin/main]", stdout, "⚠️ Vietinė šaka nėra sinchronizuota su `origin/main`! Vykdyk `git push`.")

if __name__ == "__main__":
    unittest.main()
