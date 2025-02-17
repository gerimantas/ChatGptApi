import sys
import os
import asyncio
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextBrowser, QLineEdit, QPushButton, QLabel, QComboBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSettings, QSize, QPoint

# ✅ Pridėtas šrifto dydžio nustatymas
FONT_SIZE = 14  # Galima keisti pagal poreikį

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bot_aps.core.openai_client import ask_openai, get_current_model
from bot_aps.ui.ui_config import apply_dark_theme, style_input_field, style_send_button
from ai_core.instruction_loader import switch_model, load_instructions

class ChatUI(QWidget):
    def __init__(self):
        super().__init__()
        self.settings = QSettings("bot_aps", "ChatUI")
        self.current_model = asyncio.run(get_current_model())
        self.setWindowTitle(f"AI Chat - {self.current_model}")

        self.init_ui()

    def init_ui(self):
        """Sukuriame UI komponentus su vienodu šrifto dydžiu"""
        default_size = QSize(600, 500)
        default_position = QPoint(100, 100)
        self.resize(self.settings.value("window_size", default_size, type=QSize))
        self.move(self.settings.value("window_position", default_position, type=QPoint))

        apply_dark_theme(self)

        self.layout = QVBoxLayout()
        
        # ✅ Chato lango šriftas
        self.chat_display = QTextBrowser()
        self.chat_display.setFont(QFont("Arial", FONT_SIZE))
        self.layout.addWidget(self.chat_display)

        # ✅ Modelio pasirinkimo meniu šriftas
        self.model_label = QLabel("Pasirinkite AI modelį:")
        self.model_label.setFont(QFont("Arial", FONT_SIZE))
        self.layout.addWidget(self.model_label)

        self.model_selector = QComboBox()
        self.model_selector.setFont(QFont("Arial", FONT_SIZE))
        self.available_models = self.get_available_models()
        self.model_selector.addItems(self.available_models)
        self.model_selector.setCurrentText(self.current_model)
        self.layout.addWidget(self.model_selector)

        self.model_selector.currentIndexChanged.connect(self.change_model)

        # ✅ Įvesties laukelio ir mygtuko išdėstymas
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Arial", FONT_SIZE))
        style_input_field(self.input_field)

        self.send_button = QPushButton("Send")
        self.send_button.setFont(QFont("Arial", FONT_SIZE))
        style_send_button(self.send_button)

        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.send_button)
        self.layout.addLayout(input_layout)

        self.setLayout(self.layout)

        self.send_button.clicked.connect(self.send_message)
        self.input_field.returnPressed.connect(self.send_message)

    def send_message(self):
        """Siunčiame vartotojo žinutę į OpenAI API ir rodome atsakymą."""
        user_input = self.input_field.text().strip()
        if not user_input:
            return

        if "gpt version" in user_input.lower() or "kokia gpt versija" in user_input.lower():
            real_model = asyncio.run(get_current_model())
            self.chat_display.append(f"\n💬 You: {user_input}\n🤖 AI: Šiuo metu naudoju: {real_model}.")
            self.setWindowTitle(f"AI Chat - {real_model}")
            return

        response = asyncio.run(ask_openai(user_input))
        self.chat_display.append(f"\n💬 You: {user_input}\n🤖 AI: {response}")

        self.input_field.clear()
        self.chat_display.repaint()

    def get_available_models(self):
        """Grąžina sąrašą galimų modelių iš instrukcijų failo."""
        instructions = load_instructions()
        return instructions.get("MODEL_SELECTION", {}).get("AVAILABLE_MODELS", [])

    def change_model(self):
        """Atnaujina AI modelį pagal vartotojo pasirinkimą iš UI."""
        new_model = self.model_selector.currentText()
        switch_model(new_model)
        self.current_model = new_model
        self.setWindowTitle(f"AI Chat - {self.current_model}")
        self.chat_display.append(f"🔄 AI modelis pakeistas į: {self.current_model}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatUI()
    window.show()
    sys.exit(app.exec_())
