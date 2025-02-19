import ast
import os

def analyze_code(file_path):
    """Perskaito kodą ir analizuoja klaidas."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"🔴 Klaida: Failas '{file_path}' nerastas.")
    
    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()

    issues = find_common_issues(code)
    optimizations = suggest_optimizations(code)

    return {
        "issues": issues,
        "optimizations": optimizations
    }

def find_common_issues(code):
    """Ieško dažniausiai pasitaikančių klaidų kode."""
    issues = []
    try:
        ast.parse(code)
    except SyntaxError as e:
        issues.append(f"🔴 Sintaksės klaida: {e}")

    if "eval(" in code:
        issues.append("⚠️ Naudojama `eval()`, kuri gali kelti saugumo grėsmių.")

    return issues

def suggest_optimizations(code):
    """Pateikia optimizavimo pasiūlymus."""
    suggestions = []
    if "==" in code and "is" in code:
        suggestions.append("✅ Naudok `is` vietoje `==` objektų palyginimui, jei įmanoma.")
    
    if "for " in code and "range(len(" in code:
        suggestions.append("🔹 Naudok `enumerate()` vietoje `range(len(...))`, kad kodas būtų aiškesnis.")

    return suggestions

# Testavimas
if __name__ == "__main__":
    test_file = "test_script.py"
    with open(test_file, "w") as f:
        f.write("print('Hello World')\nfor i in range(len([1,2,3])): print(i)")

    result = analyze_code(test_file)
    print(f"🔍 Aptiktos problemos: {result['issues']}")
    print(f"✨ Optimizacijos pasiūlymai: {result['optimizations']}")

