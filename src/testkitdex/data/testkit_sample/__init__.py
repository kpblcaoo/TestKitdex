"""
TestKit - Удобная инфра для тестов
Глобальные вызовы и базовые заглушки
"""

from typing import Any, Dict, List, Optional
from dataclasses import dataclass
from pathlib import Path
import json
import random
import string

# Глобальный экземпляр для удобных вызовов
class TestKit:
    """Основной класс TestKit с глобальными методами"""
    
    def __init__(self):
        self._fixtures_path = Path(__file__).parent / "fixtures"
        self._fixtures_path.mkdir(exist_ok=True)
    
    # === Базовые генераторы ===
    
    def create_user(self, **kwargs) -> Dict[str, Any]:
        """Создать пользователя"""
        user = {
            "id": random.randint(1000, 9999),
            "username": f"user_{random.randint(100, 999)}",
            "first_name": "Test",
            "last_name": "User",
            **kwargs
        }
        return user
    
    def create_message(self, **kwargs) -> Dict[str, Any]:
        """Создать сообщение"""
        message = {
            "id": random.randint(1, 1000),
            "text": "Test message",
            "user": self.create_user(),
            "chat": self.create_chat(),
            **kwargs
        }
        return message
    
    def create_chat(self, **kwargs) -> Dict[str, Any]:
        """Создать чат"""
        chat = {
            "id": random.randint(-1000000000, -1000),
            "type": "group",
            "title": "Test Group",
            **kwargs
        }
        return chat
    
    # === Файловые операции ===
    
    def save_fixture(self, name: str, data: Any) -> Path:
        """Сохранить фикстуру в JSON"""
        file_path = self._fixtures_path / f"{name}.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return file_path
    
    def load_fixture(self, name: str) -> Any:
        """Загрузить фикстуру из JSON"""
        file_path = self._fixtures_path / f"{name}.json"
        if not file_path.exists():
            raise FileNotFoundError(f"Fixture {name} not found")
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def list_fixtures(self) -> List[str]:
        """Список доступных фикстур"""
        return [f.stem for f in self._fixtures_path.glob("*.json")]
    
    # === Утилиты ===
    
    def random_string(self, length: int = 10) -> str:
        """Случайная строка"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    def random_id(self) -> int:
        """Случайный ID"""
        return random.randint(1, 999999)
    
    def create_mock(self, **kwargs) -> Dict[str, Any]:
        """Создать мок объект"""
        return {
            "id": self.random_id(),
            "name": self.random_string(),
            "data": kwargs
        }

# Глобальный экземпляр
TK = TestKit()

# Удобные алиасы
def create_user(**kwargs): return TK.create_user(**kwargs)
def create_message(**kwargs): return TK.create_message(**kwargs)
def create_chat(**kwargs): return TK.create_chat(**kwargs)
def save_fixture(name: str, data: Any): return TK.save_fixture(name, data)
def load_fixture(name: str): return TK.load_fixture(name)
def random_string(length: int = 10): return TK.random_string(length)
def random_id(): return TK.random_id()
def create_mock(**kwargs): return TK.create_mock(**kwargs)

# Экспорт для удобства
__all__ = [
    'TK', 'TestKit',
    'create_user', 'create_message', 'create_chat',
    'save_fixture', 'load_fixture',
    'random_string', 'random_id', 'create_mock'
] 