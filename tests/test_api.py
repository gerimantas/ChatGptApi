import sys
import os

# ✅ Pridedame `modules/` katalogą į `sys.path`, kad testai rastų modulius
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import asyncio
from bot_aps.core.openai_client import ask_openai

class TestOpenAIApi(unittest.TestCase):
    """Testuoja OpenAI API užklausas."""

    def test_api_response(self):
        """Testuoja, ar OpenAI API grąžina atsakymą."""
        test_message = "Kas yra Python?"
        ai_response = asyncio.run(ask_openai(test_message))

        self.assertIsInstance(ai_response, str, "❌ API turėtų grąžinti teksto eilutę.")
        self.assertGreater(len(ai_response), 0, "❌ API atsakymas neturėtų būti tuščias.")

if __name__ == "__main__":
    unittest.main()
