import time

def log_structure_change(change_desc):
    with open("structure_changes.log", "a", encoding="utf-8") as file:
        file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {change_desc}\\n")

if __name__ == "__main__":
    log_structure_change("✅ Struktūros stebėjimas pradėtas.")

