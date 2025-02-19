import json
import os

CONFIG_PATH = "config/aivolt_instructions.json"
LOG_PATHS = [
    "logs/api_usage.json",
    "logs/test_results.json",
    "logs/adaptive_learning.json"
]

def test_json_validity():
    """Patikrina, ar `aivolt_instructions.json` yra tinkamai suformatuotas"""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        try:
            json.load(f)
        except json.JSONDecodeError:
            assert False, "JSON failas turi sintaksės klaidų!"

def test_required_log_files():
    """Patikrina, ar naujai pridėti log failai yra projekte"""
    for log_path in LOG_PATHS:
        assert os.path.exists(log_path), f"Trūksta log failo: {log_path}"

def test_task_execution_priority():
    """Patikrina, ar `TASK_EXECUTION` turi prioritetus"""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)
    assert "TASK_PRIORITY" in config["TASK_EXECUTION"], "TASK_EXECUTION neturi prioriteto valdymo!"

def test_api_monitoring_enabled():
    """Patikrina, ar API stebėjimas įjungtas"""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)
    assert config["API_USAGE_MONITORING"]["ENABLED"], "API_USAGE_MONITORING nėra įjungtas!"

def test_testing_enabled():
    """Patikrina, ar įjungta testavimo sistema"""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)
    assert config["TESTING"]["ENABLED"], "TESTING nėra įjungtas!"

if __name__ == "__main__":
    test_json_validity()
    test_required_log_files()
    test_task_execution_priority()
    test_api_monitoring_enabled()
    test_testing_enabled()
    print("✅ Visi testai praėjo sėkmingai!")
