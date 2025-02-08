import os


def scan_directory(directory, output_file, indent=0, ignored_folders=None, ignored_files=None):
    """
    Rekursyviai nuskaito katalogą ir išveda struktūrą į failą, tiksliai atitinkant pateiktą vizualizaciją.
    
    :param directory: Aplanko kelias, kurį reikia nuskaityti.
    :param output_file: Failas, į kurį bus įrašoma struktūra.
    :param indent: Įtraukos lygis struktūros vizualizacijai.
    :param ignored_folders: Sąrašas aplankų, kuriuos reikia sutraukti.
    :param ignored_files: Sąrašas failų pavadinimų arba tipų, kuriuos galima praleisti.
    """
    if ignored_folders is None:
        ignored_folders = {"__pycache__", ".idea", ".vscode"}
    if ignored_files is None:
        ignored_files = {".DS_Store", "thumbs.db"}

    items = sorted(os.listdir(directory))  # Rūšiuoti pagal pavadinimą

    with open(output_file, "a", encoding="utf-8") as f:
        for item in items:
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                # Aiškiai išskleidžiami `modules/` ir `tests/` aplankai su jų turiniu
                if item == "modules" or item == "tests":
                    f.write(f"{'│   ' * indent}📂 {item}/\n")
                    sub_items = sorted(os.listdir(item_path))
                    for sub_item in sub_items:
                        sub_item_path = os.path.join(item_path, sub_item)
                        if os.path.isdir(sub_item_path):
                            f.write(f"{'│   ' * (indent + 1)}📂 {sub_item}/\n")
                        else:
                            f.write(f"{'│   ' * (indent + 1)}📄 {sub_item}\n")
                elif item == ".git":
                    f.write(f"{'│   ' * indent}📂 {item}/ ({len(os.listdir(item_path))} failai)  # Git saugykla\n")
                else:
                    f.write(f"{'│   ' * indent}📂 {item}/\n")
                    scan_directory(item_path, output_file, indent + 1, ignored_folders, ignored_files)
            else:
                f.write(f"{'│   ' * indent}📄 {item}\n")


if __name__ == "__main__":
    output_file = "project_structure_output.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("ChatGptApi/\n")
    scan_directory(os.getcwd(), output_file)
    print(f"📄 Projekto struktūra išsaugota į {output_file}")
