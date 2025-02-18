import sys
import os
import unittest
import asyncio
from unittest.mock import AsyncMock, patch
from APS_project_manager.AI_assistant.openai_client import ask_openai

# ✅ Pridedame `modules/` katalogą į `sys.path`, kad testai rastų modulius
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestOpenAIApi(unittest.TestCase):
    """Testuoja OpenAI API užklausas."""

    @patch("APS_project_manager.AI_assistant.openai_client.ask_openai", new_callable=AsyncMock)
    async def test_api_response(self, mock_openai):
        """Testuoja, ar OpenAI API grąžina atsakymą."""
        mock_openai.return_value = "Python yra programavimo kalba."

        test_message = "Kas yra Python?"
        ai_response = await ask_openai(test_message)  # 🔄 Naudojame `await` vietoje `asyncio.run()`

        self.assertIsInstance(ai_response, str, "❌ API turėtų grąžinti teksto eilutę.")
        self.assertGreater(len(ai_response), 0, "❌ API atsakymas neturėtų būti tuščias.")

if __name__ == "__main__":
    unittest.main()
