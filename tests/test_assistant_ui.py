import unittest
from unittest.mock import AsyncMock, patch
import asyncio
from bot_aps.core.assistant_ui import process_command

class TestAssistantUI(unittest.IsolatedAsyncioTestCase):

    @patch("bot_aps.core.assistant_ui.ask_openai", new_callable=AsyncMock)
    async def test_ask_command(self, mock_ask_openai):
        """Testuoja `/ask` komandą."""
        mock_ask_openai.return_value = "Test response"
        
        response = await process_command("/ask", "Kas yra Python?", {
            "/ask": "Pateik glaustą atsakymą (1-2 sakiniai):"
        }, test_mode=True)

        self.assertEqual(response, "Test response")

    @patch("bot_aps.core.assistant_ui.ask_openai", new_callable=AsyncMock)
    async def test_style_command(self, mock_ask_openai):
        """Testuoja `/style` komandą."""
        mock_ask_openai.return_value = "Styled code"
        
        response = await process_command("/style", "def example(): pass", {
            "/style": "Suformatuok šį Python kodą pagal PEP 8 standartą. Grąžink tik suformatuotą kodą:"
        }, test_mode=True)

        self.assertEqual(response, "Styled code")

    @patch("bot_aps.core.assistant_ui.ask_openai", new_callable=AsyncMock)
    async def test_test_command(self, mock_ask_openai):
        """Testuoja `/test` komandą."""
        mock_ask_openai.return_value = "Generated tests"

        response = await process_command("/test", "def test(): return True", {
            "/test": "Sugeneruok `unittest` testus šiai Python funkcijai. Grąžink tik testų kodą:"
        }, test_mode=True)

        self.assertEqual(response, "Generated tests")

if __name__ == "__main__":
    asyncio.run(unittest.main())
