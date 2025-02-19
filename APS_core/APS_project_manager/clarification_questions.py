def ask_clarifying_questions(task_data):
    """Automatiškai užduoda patikslinančius klausimus pagal vartotojo užduotį."""
    
    questions = []

    if not task_data["expected_result"]:
        questions.append("🔹 Koks yra tikslus norimas užduoties rezultatas?")
    
    if task_data["priority"] not in ["aukštas", "vidutinis", "žemas"]:
        questions.append("🔹 Nenurodėte prioriteto. Koks užduoties prioritetas?")
    
    if not task_data["deadline"]:
        questions.append("🔹 Ar yra galutinis terminas? Jei taip, nurodykite datą (YYYY-MM-DD).")

    return questions

def refine_task_entry(task_data):
    """Papildo užduoties informaciją pagal patikslinančius klausimus."""
    
    clarification_needed = ask_clarifying_questions(task_data)
    
    if not clarification_needed:
        print("\n✅ Užduotis pilnai užpildyta, nereikia papildomų klausimų.")
        return task_data

    print("\n🔍 Papildoma informacija reikalinga:")
    
    for question in clarification_needed:
        answer = input(question + " ")
        if "rezultatas" in question.lower():
            task_data["expected_result"] = answer
        elif "prioritetas" in question.lower():
            task_data["priority"] = answer.lower()
        elif "terminas" in question.lower():
            task_data["deadline"] = answer

    return task_data
