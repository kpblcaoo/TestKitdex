"""
Scenario Generator for TestKit
"""

from typing import Dict, Any, List
from faker import Faker
from ..factories import UserFactory, MessageFactory


class TestScenarioGenerator:
    """Генератор тестовых сценариев"""
    
    def __init__(self):
        self.faker = Faker()
    
    def create_simple_scenario(self) -> Dict[str, Any]:
        """Создать простой сценарий"""
        return {
            "users": [UserFactory.create_telegram_user() for _ in range(2)],
            "messages": [MessageFactory.create_telegram_message() for _ in range(3)],
            "metadata": {
                "scenario_type": "simple",
                "created_at": self.faker.date_time(),
                "description": "Простой тестовый сценарий"
            }
        }
    
    def create_complex_scenario(self) -> Dict[str, Any]:
        """Создать сложный сценарий"""
        users = [
            UserFactory.create_telegram_user(),
            UserFactory.create_admin_user(),
            UserFactory.create_bot_user()
        ]
        
        messages = [
            MessageFactory.create_command_message("/start"),
            MessageFactory.create_telegram_message(),
            MessageFactory.create_long_message(),
            MessageFactory.create_bot_message(),
            MessageFactory.create_command_message("/help")
        ]
        
        return {
            "users": users,
            "messages": messages,
            "metadata": {
                "scenario_type": "complex",
                "created_at": self.faker.date_time(),
                "description": "Сложный тестовый сценарий с разными типами данных"
            }
        }
    
    def create_performance_scenario(self, user_count: int = 10, message_count: int = 50) -> Dict[str, Any]:
        """Создать сценарий для тестирования производительности"""
        users = [UserFactory.create_telegram_user() for _ in range(user_count)]
        messages = [MessageFactory.create_telegram_message() for _ in range(message_count)]
        
        return {
            "users": users,
            "messages": messages,
            "metadata": {
                "scenario_type": "performance",
                "created_at": self.faker.date_time(),
                "description": f"Сценарий производительности: {user_count} пользователей, {message_count} сообщений"
            }
        }
    
    def create_error_scenario(self) -> Dict[str, Any]:
        """Создать сценарий с ошибками"""
        return {
            "users": [UserFactory.create_telegram_user()],
            "messages": [
                MessageFactory.create_command_message("/invalid"),
                MessageFactory.create_telegram_message(text="Error message")
            ],
            "errors": [
                {"type": "validation_error", "message": "Invalid command"},
                {"type": "permission_error", "message": "Access denied"}
            ],
            "metadata": {
                "scenario_type": "error",
                "created_at": self.faker.date_time(),
                "description": "Сценарий с ошибками"
            }
        }
    
    def create_custom_scenario(self, **kwargs) -> Dict[str, Any]:
        """Создать кастомный сценарий"""
        base_scenario = self.create_simple_scenario()
        base_scenario.update(kwargs)
        return base_scenario 