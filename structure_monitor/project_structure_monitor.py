import os
import json

def scan_main_folders(root_path, depth=2):  # Pakeistas gylis į 2
    structure = {}

    for root, dirs, files in os.walk(root_path):
        relative_path = os.path.relpath(root, root_path)
        
        # Užtikriname, kad būtų saugomi ir giliau esantys aplankai
        if relative_path.count(os.sep) < depth:
            structure[relative_path] = {"files": sorted(files)}

    return structure

if __name__ == "__main__":
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(f"🔍 Nuskaitymo kelias: {root_path}")

    # Nuskaityti dviejų lygių aplankų failus
    structure = scan_main_folders(root_path, depth=2)

    # Išsaugoti rezultatą
    snapshot_path = os.path.join(os.path.dirname(__file__), "structure_snapshot.txt")
    with open(snapshot_path, "w", encoding="utf-8") as file:
        json.dump(structure, file, indent=4, ensure_ascii=False)

    print(f"✅ Projekto dviejų lygių aplankų failų struktūra nuskaityta ir išsaugota į {snapshot_path}")
