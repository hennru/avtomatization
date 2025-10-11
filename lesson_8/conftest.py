# 08_lesson/conftest.py
# настройки для тестов YouGile API

import os
import uuid
import pytest


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL API YouGile."""
    return os.getenv("YOUGILE_BASE_URL", "https://ru.yougile.com/api-v2")


@pytest.fixture(scope="session")
def api_key():
    """API ключ для аутентификации."""
    key = os.getenv("YOUGILE_API_KEY")
    if not key:
        key =
    if not key:
        pytest.skip("Не задан YOUGILE_API_KEY — тесты пропущены.")
    return key


@pytest.fixture
def headers(api_key):
    """Заголовки с авторизацией для всех запросов."""
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


@pytest.fixture
def unique_name():
    """Генератор уникальных имён для проектов."""
    return f"pytest-project-{uuid.uuid4().hex[:8]}"
