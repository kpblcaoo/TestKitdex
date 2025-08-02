"""
User Factory using factory-boy
"""

from factory import Factory, Faker, SubFactory
from typing import Dict, Any


class UserFactory(Factory):
    """Factory for creating test users"""
    
    class Meta:
        model = dict
    
    id = Faker('random_int', min=1000, max=9999)
    username = Faker('user_name')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')
    is_active = Faker('boolean', chance_of_getting_true=90)
    created_at = Faker('date_time_this_year')
    
    @classmethod
    def create_telegram_user(cls, **kwargs) -> Dict[str, Any]:
        """Создать Telegram пользователя"""
        return cls.create(
            username=f"user_{Faker('random_int', min=100, max=999).generate()}",
            first_name="Test",
            last_name="User",
            **kwargs
        )
    
    @classmethod
    def create_admin_user(cls, **kwargs) -> Dict[str, Any]:
        """Создать админа"""
        return cls.create(
            username="admin",
            first_name="Admin",
            last_name="User",
            is_active=True,
            **kwargs
        )
    
    @classmethod
    def create_bot_user(cls, **kwargs) -> Dict[str, Any]:
        """Создать бота"""
        return cls.create(
            username="testkit_bot",
            first_name="TestKit",
            last_name="Bot",
            is_active=True,
            **kwargs
        ) 