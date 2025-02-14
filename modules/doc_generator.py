# Failas: modules/doc_generator.py
import os
import ast
from ai.assist.core.openai_client import ask_openai

def generate_docstring(source_code):
    """Siunčia kodą į OpenAI API ir sugeneruoja docstring'ą."""
    prompt = f"Generuok PEP 257 formato docstring'ą šiai Python funkcijai arba klasei:\n```python\n{source_code}\n```"
    return ask_openai(prompt)

def process_file(file_path):
    """Apdoroja Python failą, prideda trūkstamus docstring'us."""
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)
    new_lines = source.splitlines()

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if not ast.get_docstring(node):
                start_line = node.lineno - 1
                generated_doc = generate_docstring(ast.unparse(node))
                new_lines.insert(start_line + 1, f'    """{generated_doc}"""')

    updated_code = "\n".join(new_lines)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_code)

def process_directory(directory):
    """Iteruoja per visus Python failus kataloge ir generuoja dokumentaciją."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and file != "doc_generator.py":
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    process_directory("modules")
    print("✅ Dokumentacija sugeneruota visiems Python failams!")

