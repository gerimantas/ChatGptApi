import json
import os
from typing import Dict

class DecisionMaker:
    def __init__(self, data_file='APS_project_manager/APS_strategy/strategy_data.json'):
        self.data_file = data_file
        self.strategy = self._load_strategy()

    def _load_strategy(self) -> Dict:
        """Įkelia esamus strategijos duomenis iš JSON failo."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_strategy(self):
        """Išsaugo strategijos duomenis į JSON failą."""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.strategy, f, indent=4, ensure_ascii=False)

    def define_plan(self, task_id: int, analysis: str, priority: str = 'medium'):
        """Sukuria veiksmų planą užduočiai."""
        self.strategy[task_id] = {
            "analysis": analysis,
            "priority": priority,
            "status": "planned"
        }
        self.save_strategy()
        return self.strategy[task_id]

    def update_status(self, task_id: int, new_status: str):
        """Atnaujina užduoties strategijos būseną."""
        if task_id in self.strategy:
            self.strategy[task_id]["status"] = new_status
            self.save_strategy()
            return self.strategy[task_id]
        return None
