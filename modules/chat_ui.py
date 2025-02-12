import sys
import os
import json
import asyncio
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextBrowser, QLineEdit, QPushButton
from PyQt5.QtCore import QSettings, QSize, QPoint

# ✅ Užtikriname, kad `modules/` katalogas būtų matomas kaip paketas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.openai_client import ask_openai, get_current_model
from modules.ui_config import apply_dark_theme, style_input_field, style_send_button

class ChatUI(QWidget):
    def __init__(self):
        super().__init__()
        self.settings = QSettings("ai.assist", "ChatUI")

        # ✅ Gauti realią GPT modelio versiją iš OpenAI API
        self.current_model = asyncio.run(get_current_model())
        self.setWindowTitle(f"AI Chat - {self.current_model}")

        # ✅ UI komponentai
        self.init_ui()

    def init_ui(self):
        """Sukuriame UI komponentus"""
        default_size = QSize(600, 500)
        default_position = QPoint(100, 100)
        self.resize(self.settings.value("window_size", default_size, type=QSize))
        self.move(self.settings.value("window_position", default_position, type=QPoint))

        # ✅ Pritaikome tamsią temą iš `ui_config.py`
        apply_dark_theme(self)

        # ✅ UI išdėstymas
        self.layout = QVBoxLayout()
        self.chat_display = QTextBrowser()
        self.layout.addWidget(self.chat_display)

        # ✅ Įvesties laukas ir `Send` mygtukas vienoje eilėje
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        style_input_field(self.input_field)
        self.send_button = QPushButton("Send")
        style_send_button(self.send_button)

        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.send_button)
        self.layout.addLayout(input_layout)

        self.setLayout(self.layout)

        # ✅ Susiejame įvykius su metodais
        self.send_button.clicked.connect(self.send_message)
        self.input_field.returnPressed.connect(self.send_message)

    def send_message(self):
        """Siunčiame vartotojo žinutę į OpenAI API ir rodome atsakymą."""
        user_input = self.input_field.text().strip()
        if not user_input:
            return

        # ✅ Jei vartotojas klausia apie GPT modelio versiją, grąžiname realią API grąžintą versiją
        if "gpt version" in user_input.lower() or "kokia gpt versija" in user_input.lower():
            real_model = asyncio.run(get_current_model())
            self.chat_display.append(f"\n💬 You: {user_input}\n🤖 AI: Šiuo metu naudoju: {real_model}.")
            self.setWindowTitle(f"AI Chat - {real_model}")  # ✅ Atnaujiname viršutinės juostos pavadinimą
            return

        # ✅ Siunčiame užklausą į OpenAI API
        response = asyncio.run(ask_openai(user_input))
        self.chat_display.append(f"\n💬 You: {user_input}\n🤖 AI: {response}")

        # ✅ Stabilizuojame UI po įvesties
        self.input_field.clear()
        self.input_field.setMinimumHeight(50)
        self.input_field.adjustSize()
        self.chat_display.repaint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatUI()
    window.show()
    sys.exit(app.exec_())
