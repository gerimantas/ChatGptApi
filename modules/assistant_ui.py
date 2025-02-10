import sys
import os
import asyncio

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from modules.openai_client import ask_openai  

async def start_chat():
    """Paleidžia AI asistentą terminale."""
    print("🚀 START CHAT")
    await main()

async def get_multiline_input(prompt):
    """Leidžia įvesti kelias kodo eilutes, baigiamas su `/done`."""
    print(f"✏️ PRADEDAMAS ĮVESTIES RINKIMAS: {prompt}")
    lines = []
    while True:
        line = input()
        if line.strip().lower() == "/done":
            break
        lines.append(line)
    print(f"✅ ĮVESTIES RINKIMAS BAIGTAS, gautas kodas: {lines}")
    return "\n".join(lines) if lines else None

async def process_command(command, code_text, commands_map, test_mode=False):
    """Apdoroja komandą ir siunčia užklausą į OpenAI API."""
    print(f"➡️ ENTER process_command: `{command}`")  
    print(f"🔹 Testavimo režimas: {test_mode}")

    if command not in commands_map:
        print(f"⚠️ ERROR: `{command}` nėra žinomas!")
        print("⬅️ EXIT process_command (invalid command)")
        return None

    print(f"⏳ AI analizuoja {command}...")
    print(f"📌 Komandų žemėlapis: {commands_map}")
    print(f"🔍 Rasta komanda: {commands_map[command]}")

    print("🛠️ `ask_openai()` turėtų būti kviečiamas dabar!")
    result = await ask_openai(f"{commands_map[command]}\n```python\n{code_text}\n```")  
    print("🛠️ `ask_openai()` buvo iškviestas!")  
    print(f"📄 {result}\n")

    print("⬅️ EXIT process_command")  
    return result

async def main(test_mode=False):
    """Pagrindinė AI asistento funkcija. Jei `test_mode=True`, `SystemExit` nėra iškviečiamas."""
    print(f"🔹 ENTER main() (test_mode={test_mode})")
    commands_map = {
        "/ask": "Pateik glaustą atsakymą (1-2 sakiniai):",
        "/fix": "Pataisyk klaidas šiame Python kode ir grąžink tik pataisytą kodą:",
        "/refactor": "Optimizuok šį Python kodą, išlaikydamas jo veikimą. Grąžink tik optimizuotą kodą:",
        "/test": "Sugeneruok `unittest` testus šiai Python funkcijai. Grąžink tik testų kodą:",
        "/doc": "Sugeneruok PEP 257 standarto docstring šiai Python funkcijai. Grąžink tik dokumentaciją:",
        "/style": "Suformatuok šį Python kodą pagal PEP 8 standartą. Grąžink tik suformatuotą kodą:",
        "/explain": "Pateik glaustą šio kodo paaiškinimą (1–2 sakiniai):"
    }

    print("🔹 AI Asistentas – įveskite komandą (/ask, /fix, /refactor, /test, /doc, /style, /explain, /exit)")

    while True:
        command = input("🖥️ >>> ").strip().lower()
        print(f"🔹 Gauta komanda: `{command}`")

        if command == "/exit":
            print("👋 Išeinama iš AI asistento...")
            if not test_mode:
                raise SystemExit
            else:
                print("✅ Testavimo režime – ciklas baigtas.")
                break

        elif command in commands_map:
            code_text = await get_multiline_input(f"🔹 Įveskite Python kodą. Baigti įvestį – `/done`.")
            await process_command(command, code_text, commands_map, test_mode)
        else:
            print("⚠️ Neatpažinta komanda! Bandykite dar kartą.")

    print("⬅️ EXIT main()")  

# ✅ Užtikrina, kad skriptas būtų paleidžiamas teisingai
if __name__ == "__main__":
    asyncio.run(main())
