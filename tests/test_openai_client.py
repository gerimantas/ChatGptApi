import sys
import os
import pytest
import asyncio
from cachetools import LRUCache

# ✅ Naudojame absoliutų kelią į `APS_project_manager.AI_assistant/`
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CORE_PATH = os.path.join(PROJECT_ROOT, "bot_aps", "core")

if CORE_PATH not in sys.path:
    print(f"🔹 Pridedame `APS_project_manager.AI_assistant/` į sys.path: {CORE_PATH}")
    sys.path.insert(0, CORE_PATH)

try:
    from APS_project_manager.AI_assistant.openai_client import ask_openai
except ModuleNotFoundError as e:
    print(f"⚠️ Importo klaida: {e}")
    print(f"🔍 sys.path: {sys.path}")
    raise

@pytest.mark.asyncio
async def test_openai_response():
    """Testuoja, ar OpenAI API grąžina atsakymą."""
    prompt = "Koks yra Žemės palydovas?"
    response = await ask_openai(prompt)
    assert isinstance(response, str) and len(response) > 0

@pytest.mark.asyncio
async def test_openai_cache():
    """Testuoja, ar užklausa išsaugoma LRU cache."""
    prompt = "Kas yra Python?"
    cache = LRUCache(maxsize=100)
    response1 = await ask_openai(prompt)
    cache[prompt] = response1
    response2 = cache.get(prompt)
    assert response1 == response2
