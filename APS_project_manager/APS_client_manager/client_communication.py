import json
import os

class ClientCommunication:
    def __init__(self, data_file='APS_project_manager/APS_client_manager/client_data.json'):
        self.data_file = data_file
        self.clients = self._load_clients()

    def _load_clients(self):
        """Įkelia klientų duomenis iš JSON failo."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_clients(self):
        """Išsaugo klientų duomenis į JSON failą."""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.clients, f, indent=4, ensure_ascii=False)

    def receive_request(self, client_id, request):
        """Priima kliento užklausą ir ją registruoja."""
        if client_id not in self.clients:
            self.clients[client_id] = []
        self.clients[client_id].append({"request": request, "status": "received"})
        self.save_clients()
        return {"message": "Užklausa priimta", "client_id": client_id}

    def send_response(self, client_id, response):
        """Siunčia atsakymą klientui."""
        if client_id in self.clients and self.clients[client_id]:
            self.clients[client_id][-1]["response"] = response
            self.clients[client_id][-1]["status"] = "responded"
            self.save_clients()
            return {"message": "Atsakymas išsiųstas", "client_id": client_id}
        return {"error": "Klientas nerastas arba nėra aktyvios užklausos"}
