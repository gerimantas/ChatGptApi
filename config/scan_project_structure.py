import os

def scan_directory(directory, prefix=""):
    """Rekursyviai nuskaityti direktorijų struktūrą ir formatuoti kaip pateiktoje nuotraukoje."""
    entries = sorted(os.listdir(directory))
    result = []
    
    for index, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        is_last = (index == len(entries) - 1)
        branch = "|-- " if not is_last else "|__ "
        result.append(f"{prefix}{branch}{entry}")
        
        if os.path.isdir(path):
            extension = "|   " if not is_last else "    "
            result.extend(scan_directory(path, prefix + extension))
    
    return result

def save_structure(output_file):
    """Išsaugo nuskaitytą struktūrą į failą."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Projekto šaknis
    structure = scan_directory(base_dir)
    
    output_path = os.path.join(base_dir, "config", output_file)
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("\n".join(structure) + "\n")
    
    print(f"✅ Failas išsaugotas: {output_path}")

if __name__ == "__main__":
    save_structure("ai_structure.txt")
