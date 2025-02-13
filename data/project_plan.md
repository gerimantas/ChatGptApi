Set-Content -Path "project_plan.md" -Value @'
# 📌 OPTIMIZUOTAS „ai.assist“ PROJEKTO PLANAS

🔹 **Tikslas:** Užtikrinti, kad ChatGPT nepasiūlytų jau atliktų veiksmų, optimizuoti OpenAI API naudojimą ir automatizuoti kodo testavimą bei versijų valdymą.

---

## **1️⃣ BŪTINIAUSI DARBAI (AUKŠČIAUSIAS PRIORITETAS)**
✅ **1.1. OpenAI API optimizacija**
🔹 Failas: `openai_client.py`
- [x] Pridėtas `rate limiting`
- [x] Įdiegtas `cache` mechanizmas per `shelve`
- [x] Klaidos tvarkymas (`RateLimitError`, `TimeoutError`)

✅ **1.2. VS Code UI sąsajos kūrimas**
🔹 Failas: `assistant_ui.py`
- [x] Komandos (`/ask`, `/fix`, `/test`, `/explain`)
- [x] Kodo įkėlimas per terminalą (`get_multiline_input`)
- [x] OpenAI API atsakymai realiuoju laiku

✅ **1.3. Failų valdymas AI pagalba**
🔹 Failas: `file_manager.py`
- [x] Failų atidarymas, redagavimas, išsaugojimas
- [x] Pakeitimų stebėjimas (`watchdog` biblioteka)

---

## **2️⃣ PATOBULINIMAI (VIDUTINIS PRIORITETAS)**
✅ **2.1. AI kodo analizė ir klaidų taisymas**
🔹 Failas: `code_analyzer.py`
- [x] Kodo sintaksės klaidų aptikimas
- [x] AI optimizuojamas kodas

✅ **2.2. Automatinis testavimas**
🔹 Failai: `tests/` katalogas
- [x] `unittest` pagrindu sukurtos testų klasės
- [x] **Privalomas testavimas prieš `commit`** (naudojant `pre-commit hook`)     

✅ **2.3. Git optimizacija AI pagalba**
🔹 Failas: `git_manager.py`
- [x] AI sugeneruotos `commit` santraukos
- [x] `.gitignore` korekcijos

✅ **2.4. Projekto failų būsenos fiksavimas**
🔹 Failas: `file_hashes.txt`
- [x] Visų failų kontrolinės sumos (`hash`)
- [x] **Panaikinta ChatGPT problema – AI nebekartoja veiksmų**

---

## **3️⃣ PAPILDOMI PATOGUMAI (ŽEMESNIS PRIORITETAS)**
✅ **3.1. Automatinė dokumentacijos generavimo sistema**
🔹 Failas: `doc_generator.py`
- [x] AI generuoja `docstring` pagal PEP 257

✅ **3.2. Progreso sekimo sistema**
🔹 Failas: `task_manager.py`
- [x] AI seka progreso %
- [x] Automatiniai `status report`

---

## **📌 GALUTINĖ IŠVADA**
🚀 **Ką vykdome dabar?**
1️⃣ **Vykdyti naują testavimą (`python -m unittest discover -s tests`)**
2️⃣ **Pridėti AI pagrindu generuojamą dokumentaciją (`doc_generator.py`)**       
3️⃣ **Įdiegti papildomą progreso sekimo mechanizmą (`task_manager.py`)**
'@

