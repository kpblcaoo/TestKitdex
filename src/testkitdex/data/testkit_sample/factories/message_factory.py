"""
Message Factory using factory-boy
"""

from factory import Factory, Faker, SubFactory
from typing import Dict, Any
from .user_factory import UserFactory


class MessageFactory(Factory):
    """Factory for creating test messages"""
    
    class Meta:
        model = dict
    
    id = Faker('random_int', min=1, max=1000)
    text = Faker('sentence', nb_words=5)
    user = SubFactory(UserFactory)
    chat_id = Faker('random_int', min=-1000000000, max=-1000)
    date = Faker('date_time_this_month')
    is_forwarded = Faker('boolean', chance_of_getting_true=20)
    is_reply = Faker('boolean', chance_of_getting_true=15)
    
    @classmethod
    def create_telegram_message(cls, **kwargs) -> Dict[str, Any]:
        """Создать Telegram сообщение"""
        return cls.create(
            text="Test message",
            user=UserFactory.create_telegram_user(),
            chat_id=-1001234567890,
            **kwargs
        )
    
    @classmethod
    def create_command_message(cls, command: str = "/start", **kwargs) -> Dict[str, Any]:
        """Создать сообщение с командой"""
        return cls.create(
            text=command,
            user=UserFactory.create_telegram_user(),
            **kwargs
        )
    
    @classmethod
    def create_long_message(cls, **kwargs) -> Dict[str, Any]:
        """Создать длинное сообщение"""
        return cls.create(
            text=Faker('paragraph', nb_sentences=3).generate(),
            user=UserFactory.create_telegram_user(),
            **kwargs
        )
    
    @classmethod
    def create_bot_message(cls, **kwargs) -> Dict[str, Any]:
        """Создать сообщение от бота"""
        return cls.create(
            text="Bot response",
            user=UserFactory.create_bot_user(),
            **kwargs
        ) 