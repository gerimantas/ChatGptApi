Write-Host "🔄 Generuojami sesijos perkėlimo failai..."

# 1️⃣ Sukuriame pagrindinį sesijos duomenų failą
"=== COINARBITR SESIJOS SANTRAUKA ===" | Out-File session_context.txt
"Data: $(Get-Date)" | Out-File -Append session_context.txt
"" | Out-File -Append session_context.txt

# 2️⃣ Įrašome atliktų darbų sąrašą
"=== ATLIKTI DARBAI ===" | Out-File -Append session_context.txt
git log --oneline -10 | Out-File -Append session_context.txt
"" | Out-File -Append session_context.txt

# 3️⃣ Įrašome projekto struktūrą
"=== PROJEKTO STRUKTŪRA ===" | Out-File -Append session_context.txt
Get-ChildItem -Recurse | Format-Table -AutoSize | Out-File project_structure.txt
Get-Content project_structure.txt | Out-File -Append session_context.txt
"" | Out-File -Append session_context.txt

# 4️⃣ Įrašome paskutinių `unittest` testų rezultatus
"=== UNITTEST TESTAVIMO ISTORIJA ===" | Out-File -Append session_context.txt
python -m unittest discover -v | Out-File tests/logs/test_results_latest.txt
Get-Content tests/logs/test_results_latest.txt | Out-File -Append session_context.txt
"" | Out-File -Append session_context.txt

# 5️⃣ Įrašome backlog informaciją
"=== NEATLIKTI DARBAI ===" | Out-File -Append session_context.txt
Get-Content backlog.txt | Out-File -Append session_context.txt
"" | Out-File -Append session_context.txt

# 6️⃣ Įrašome paskutinę `Git` būklę
"=== GIT STATUS ===" | Out-File -Append session_context.txt
git status | Out-File -Append session_context.txt
"" | Out-File -Append session_context.txt

"=== GIT LOG (PASKUTINIAI 5 COMMIT'AI) ===" | Out-File -Append session_context.txt
git log --oneline -5 | Out-File -Append session_context.txt
"" | Out-File -Append session_context.txt

# 7️⃣ Commit'iname ir išsaugome visus duomenis
Write-Host "🔄 Commit'iname visus sesijos failus į `GitHub`..."
git add session_context.txt project_structure.txt backlog.txt README.md CHANGELOG.md requirements.txt .gitignore setup.py
git commit -m "🔄 Atnaujinti visi CoinArbitr failai prieš naują sesiją (be file_hashes.txt)"
git push origin v1.2-development

Write-Host "✅ Sesijos duomenys paruošti naujai CoinArbitr sesijai!"
