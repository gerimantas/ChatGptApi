import unittest
from unittest.mock import patch
from modules.assistant_ui import process_command

class TestAssistantUI(unittest.TestCase):

    @patch("modules.assistant_ui.ask_openai")
    def test_ask_command(self, mock_ask_openai):
        """Testuoja `/ask` komandą."""
        mock_ask_openai.return_value = "Test response"
        
        process_command("/ask", "Kas yra Python?", {
            "/ask": "Pateik glaustą atsakymą (1-2 sakiniai):"
        }, test_mode=True)

        mock_ask_openai.assert_called_once()

    @patch("modules.assistant_ui.ask_openai")
    def test_style_command(self, mock_ask_openai):
        """Testuoja `/style` komandą."""
        mock_ask_openai.return_value = "Styled code"
        
        process_command("/style", "def example(): pass", {
            "/style": "Suformatuok šį Python kodą pagal PEP 8 standartą. Grąžink tik suformatuotą kodą:"
        }, test_mode=True)

        mock_ask_openai.assert_called_once()

    @patch("modules.assistant_ui.ask_openai")
    def test_test_command(self, mock_ask_openai):
        """Testuoja `/test` komandą."""
        mock_ask_openai.return_value = "Generated tests"

        process_command("/test", "def test(): return True", {
            "/test": "Sugeneruok `unittest` testus šiai Python funkcijai. Grąžink tik testų kodą:"
        }, test_mode=True)

        mock_ask_openai.assert_called_once()

    @patch("modules.assistant_ui.ask_openai")
    def test_fix_command(self, mock_ask_openai):
        """Testuoja `/fix` komandą."""
        mock_ask_openai.return_value = "Fixed code"
        
        process_command("/fix", "def example(): pass", {
            "/fix": "Pataisyk šį Python kodą ir pateik tik pataisytą versiją:"
        }, test_mode=True)

        mock_ask_openai.assert_called_once()

    @patch("modules.assistant_ui.ask_openai")
    def test_refactor_command(self, mock_ask_openai):
        """Testuoja `/refactor` komandą."""
        mock_ask_openai.return_value = "Refactored code"
        
        process_command("/refactor", "def example(): pass", {
            "/refactor": "Refaktorizuok šį Python kodą ir pateik tik refaktorizuotą versiją:"
        }, test_mode=True)

        mock_ask_openai.assert_called_once()

    @patch("modules.assistant_ui.ask_openai")
    def test_doc_command(self, mock_ask_openai):
        """Testuoja `/doc` komandą."""
        mock_ask_openai.return_value = '"""This function adds two numbers."""'
        
        process_command("/doc", "def add(a, b): return a + b", {
            "/doc": "Sugeneruok šiai funkcijai dokumentaciją ir grąžink tik docstring:"
        }, test_mode=True)

        mock_ask_openai.assert_called_once()

if __name__ == "__main__":
    unittest.main()
