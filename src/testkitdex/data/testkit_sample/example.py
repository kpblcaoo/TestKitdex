"""
Пример использования TestKit
"""

from . import TK, create_user, create_message, save_fixture, load_fixture
from .di import register, resolve, create_mock

def example_usage():
    """Пример использования TestKit"""
    
    # === Базовые генераторы ===
    user = create_user(username="john_doe", first_name="John")
    message = create_message(text="Hello, world!")
    chat = TK.create_chat(title="Test Group")
    
    print("Generated user:", user)
    print("Generated message:", message)
    print("Generated chat:", chat)
    
    # === Файловые операции ===
    save_fixture("test_user", user)
    saved_user = load_fixture("test_user")
    print("Saved and loaded user:", saved_user)
    
    # === DI контейнер ===
    class TestService:
        def __init__(self, name: str = "default"):
            self.name = name
        
        def hello(self):
            return f"Hello from {self.name}"
    
    # Регистрируем сервис
    register(TestService, TestService("test"))
    
    # Получаем сервис
    service = resolve(TestService)
    print("Service:", service.hello())
    
    # Создаём мок
    mock_service = create_mock(TestService)
    print("Mock service:", mock_service)

if __name__ == "__main__":
    example_usage() 