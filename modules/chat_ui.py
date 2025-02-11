from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextBrowser, QLineEdit, QPushButton
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import QSettings, QSize, QPoint
import sys
import json
import os
from modules.openai_client import ask_openai

class ChatUI(QWidget):
    def __init__(self):
        super().__init__()
        self.settings = QSettings("ai.assist", "ChatUI")
        self.setWindowTitle("AI Chat")
        
        # Įkeliame paskutinę lango poziciją ir dydį, jei jų nėra, naudojame numatytąsias reikšmes
        default_size = QSize(500, 600)
        default_position = QPoint(100, 100)
        self.resize(self.settings.value("window_size", default_size, type=QSize))
        self.move(self.settings.value("window_position", default_position, type=QPoint))
        
        # Nustatome tamsią temą
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))
        palette.setColor(QPalette.WindowText, QColor(200, 200, 200))
        palette.setColor(QPalette.Base, QColor(50, 50, 50))
        palette.setColor(QPalette.Text, QColor(220, 220, 220))
        self.setPalette(palette)
        
        self.layout = QVBoxLayout()
        self.chat_display = QTextBrowser()
        self.input_field = QLineEdit()
        self.send_button = QPushButton("Send")
        
        # Nustatome didesnį mygtuką su ryškesniu šriftu ir atspalviu
        self.send_button.setStyleSheet(
            "background-color: #555555; color: white; font-size: 16px; font-weight: bold; padding: 10px;"
        )
        
        self.layout.addWidget(self.chat_display)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.send_button)
        
        self.setLayout(self.layout)
        
        self.send_button.clicked.connect(self.send_message)
        self.input_field.returnPressed.connect(self.send_message)
        
        self.load_chat_history()
    
    def closeEvent(self, event):
        """Išsaugome paskutinę lango poziciją ir dydį prieš uždarant."""
        self.settings.setValue("window_size", self.size())
        self.settings.setValue("window_position", self.pos())
        self.settings.sync()
        event.accept()
    
    def load_chat_history(self, file_path="chat_history.json"):
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                history = json.load(f)
                for message in history:
                    self.chat_display.append(f"\n💬 You: {message['user']}\n🤖 AI: {message['ai']}")
    
    def save_chat_history(self, history, file_path="chat_history.json"):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
    
    def send_message(self):
        user_input = self.input_field.text()
        if not user_input.strip():
            return
        
        response = ask_openai(user_input)
        self.chat_display.append(f"\n💬 You: {user_input}\n🤖 AI: {response}")
        
        chat_history = self.load_existing_history()
        chat_history.append({"user": user_input, "ai": response})
        self.save_chat_history(chat_history)
        
        self.input_field.clear()
    
    def load_existing_history(self, file_path="chat_history.json"):
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatUI()
    window.show()
    sys.exit(app.exec_())

