## 🔄 Git Hooks aktyvavimas

Po projekto klonavimo, paleiskite šią komandą, kad `pre-commit` būtų įtrauktas į `.git/hooks/`:

```sh
cp hooks/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
