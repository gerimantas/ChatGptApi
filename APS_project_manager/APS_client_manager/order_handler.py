import json
import os

class OrderHandler:
    def __init__(self, data_file='APS_project_manager/APS_client_manager/client_data.json'):
        self.data_file = data_file
        self.orders = self._load_orders()

    def _load_orders(self):
        """Įkelia esamus užsakymus iš JSON failo."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def save_orders(self):
        """Išsaugo užsakymus į JSON failą."""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.orders, f, indent=4, ensure_ascii=False)

    def add_order(self, client_id, description, priority='medium'):
        """Prideda naują kliento užsakymą."""
        order = {
            "id": len(self.orders) + 1,
            "client_id": client_id,
            "description": description,
            "priority": priority,
            "status": "pending"
        }
        self.orders.append(order)
        self.save_orders()
        return order

    def list_orders(self, status=None):
        """Gražina visus užsakymus arba filtruotus pagal statusą."""
        if status:
            return [order for order in self.orders if order["status"] == status]
        return self.orders

    def update_order_status(self, order_id, new_status):
        """Atnaujina užsakymo būseną."""
        for order in self.orders:
            if order["id"] == order_id:
                order["status"] = new_status
                self.save_orders()
                return order
        return None
