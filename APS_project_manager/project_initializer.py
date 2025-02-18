import json
import os
from typing import Dict

class ProjectInitializer:
    def __init__(self, data_file='APS_project_manager/project_data.json'):
        self.data_file = data_file
        self.projects = self._load_projects()

    def _load_projects(self) -> Dict:
        """Įkelia esamus projektų duomenis iš JSON failo."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_projects(self):
        """Išsaugo projektų duomenis į JSON failą."""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.projects, f, indent=4, ensure_ascii=False)

    def create_project(self, project_id: int, name: str, client_id: int):
        """Sukuria naują projektą ir įrašo į duomenų bazę."""
        self.projects[project_id] = {
            "name": name,
            "client_id": client_id,
            "status": "initialized"
        }
        self.save_projects()
        return self.projects[project_id]

    def update_project_status(self, project_id: int, new_status: str):
        """Atnaujina projekto būseną."""
        if project_id in self.projects:
            self.projects[project_id]["status"] = new_status
            self.save_projects()
            return self.projects[project_id]
        return None
