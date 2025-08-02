"""
Создание структуры TestKit по образцу C# проекта
"""

from pathlib import Path
import os

def create_testkit_structure():
    """Создать структуру TestKit как в ClubDoorman"""
    base = Path("data/testkit_sample")
    
    # Основные папки TestKit
    folders = [
        "builders",           # Fluent API builders
        "services",           # Сервисные билдеры
        "infra",             # Инфраструктура
        "scenarios",          # Готовые сценарии
        "golden_master",     # Golden Master тесты
        "factories",          # Фабрики данных
        "mocks",             # Моки
    ]
    
    # Подпапки
    subfolders = {
        "builders": ["mock_builders"],
        "infra": ["auto_fixture", "bogus", "mocks"],
        "services": ["moderation", "captcha", "admin"],
    }
    
    for folder in folders:
        folder_path = base / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # Создаём __init__.py
        init_file = folder_path / "__init__.py"
        if not init_file.exists():
            init_file.write_text('"""Generated TestKit folder"""\n')
        
        print(f"Created: {folder_path}")
        
        # Создаём подпапки
        if folder in subfolders:
            for subfolder in subfolders[folder]:
                subfolder_path = folder_path / subfolder
                subfolder_path.mkdir(exist_ok=True)
                
                sub_init_file = subfolder_path / "__init__.py"
                if not sub_init_file.exists():
                    sub_init_file.write_text('"""Generated TestKit subfolder"""\n')
                
                print(f"  └── {subfolder_path}")

def create_testkit_files():
    """Создать основные файлы TestKit"""
    base = Path("data/testkit_sample")
    
    # Основные файлы (аналоги C# TestKit)
    files = {
        "testkit_main.py": '''"""
Основной модуль TestKit
Аналог TestKit.Main.cs
"""
from . import TK

# Основные методы
def create_user(**kwargs):
    return TK.create_user(**kwargs)

def create_message(**kwargs):
    return TK.create_message(**kwargs)

def create_chat(**kwargs):
    return TK.create_chat(**kwargs)
''',
        
        "testkit_builders.py": '''"""
Fluent API builders
Аналог TestKit.Builders.cs
"""
class MessageBuilder:
    def __init__(self):
        self._message = {}
    
    def with_text(self, text):
        self._message["text"] = text
        return self
    
    def from_user(self, user_id):
        self._message["user_id"] = user_id
        return self
    
    def in_chat(self, chat_id):
        self._message["chat_id"] = chat_id
        return self
    
    def build(self):
        return self._message
''',
        
        "testkit_specialized.py": '''"""
Специализированные генераторы
Аналог TestKit.Specialized.cs
"""
class Specialized:
    def __init__(self):
        self.captcha = CaptchaSpecialized()
        self.moderation = ModerationSpecialized()
        self.admin = AdminSpecialized()

class CaptchaSpecialized:
    def bait(self):
        return {"type": "captcha", "action": "bait"}
    
    def valid(self):
        return {"type": "captcha", "action": "valid"}

class ModerationSpecialized:
    def allow(self):
        return {"action": "allow"}
    
    def ban(self):
        return {"action": "ban"}

class AdminSpecialized:
    def approve_callback(self):
        return {"type": "callback", "action": "approve"}
''',
        
        "testkit_mocks.py": '''"""
Моки сервисов
Аналог TestKit.Mocks.cs
"""
class MockService:
    def __init__(self, name="MockService"):
        self.name = name
    
    def mock_method(self):
        return f"Mock result from {self.name}"

def create_mock_service(service_type, **kwargs):
    return MockService(**kwargs)
''',
        
        "testkit_facade.py": '''"""
Фасад для TestKit
Аналог TestKit.Facade.cs
"""
from .testkit_main import *
from .testkit_specialized import Specialized

class TestKitFacade:
    def __init__(self):
        self.specialized = Specialized()
    
    def create_user(self, **kwargs):
        return create_user(**kwargs)
    
    def create_message(self, **kwargs):
        return create_message(**kwargs)

# Глобальный фасад
TK = TestKitFacade()
''',
        
        "index.json": '''{
  "version": "1.0.0",
  "generators": {
    "basic": ["create_user", "create_message", "create_chat"],
    "specialized": ["captcha", "moderation", "admin"]
  },
  "tags": {
    "basic": ["user", "message", "chat"],
    "telegram": ["telegram", "bot", "api"],
    "moderation": ["moderation", "ban", "allow"],
    "captcha": ["captcha", "bait", "valid"]
  }
}''',
        
        "INDEX.md": '''# TestKit Index

## Основные методы
- `create_user()` - Создать пользователя
- `create_message()` - Создать сообщение
- `create_chat()` - Создать чат

## Специализированные
- `specialized.captcha.bait()` - Капча-приманка
- `specialized.moderation.ban()` - Бан пользователя
- `specialized.admin.approve_callback()` - Одобрение админом

## Теги
- `basic` - Базовые генераторы
- `telegram` - Telegram объекты
- `moderation` - Модерация
- `captcha` - Капча
'''
    }
    
    for filename, content in files.items():
        file_path = base / filename
        file_path.write_text(content)
        print(f"Created: {file_path}")

if __name__ == "__main__":
    create_testkit_structure()
    create_testkit_files()
    print("TestKit structure created successfully!") 