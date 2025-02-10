# 🚀 ChatGptApi

**ChatGptApi** – tai projektas, leidžiantis integruoti OpenAI API į terminalo aplinką ir atlikti įvairias kodo optimizavimo užduotis.

---

## 📌 Funkcionalumas
- ✅ Automatinis kodo taisymas (`/fix`)
- ✅ Kodo refaktorizavimas (`/refactor`)
- ✅ `unittest` testų generavimas (`/test`)
- ✅ Docstring generavimas (`/doc`)
- ✅ PEP 8 kodo formatavimas (`/style`)
- ✅ Kodo paaiškinimas (`/explain`)

---

## 🚀 Versija 1.0.1
- Įdiegta `async/await` OpenAI užklausoms.
- Optimizuoti testai ir klaidų taisymai.
- Pagerintas `assistant_ui.py` veikimas.

---

## 🔄 Git Hooks aktyvavimas

Po projekto klonavimo, paleiskite šią komandą, kad `pre-commit` būtų įtrauktas į `.git/hooks/`:

```sh
cp hooks/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
