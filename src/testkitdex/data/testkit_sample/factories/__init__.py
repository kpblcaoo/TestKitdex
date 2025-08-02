"""
TestKit Factories using factory-boy
"""

from .user_factory import UserFactory
from .message_factory import MessageFactory
from .csharp_factories import CSharpMethodFactory
from .code_factories import CSharpCodeFactory

# Глобальные factories
user_factory = UserFactory()
message_factory = MessageFactory()
csharp_method_factory = CSharpMethodFactory()
csharp_code_factory = CSharpCodeFactory()

# Удобные функции для Telegram/User
def create_user(**kwargs):
    """Создать пользователя"""
    return user_factory(**kwargs)

def create_message(**kwargs):
    """Создать сообщение"""
    return message_factory(**kwargs)

def create_telegram_user(**kwargs):
    """Создать Telegram пользователя"""
    return UserFactory.create_telegram_user(**kwargs)

def create_telegram_message(**kwargs):
    """Создать Telegram сообщение"""
    return MessageFactory.create_telegram_message(**kwargs)

def create_command_message(command: str = "/start", **kwargs):
    """Создать сообщение с командой"""
    return MessageFactory.create_command_message(command, **kwargs)

def create_bot_message(**kwargs):
    """Создать сообщение от бота"""
    return MessageFactory.create_bot_message(**kwargs)

# Удобные функции для C# методов (совместимость)
def create_user_factory():
    """Создать метод фабрики пользователя (совместимость)"""
    return CSharpMethodFactory.create_user_factory_method()

def create_message_factory():
    """Создать метод фабрики сообщения (совместимость)"""
    return CSharpMethodFactory.create_message_factory_method()

def create_generic_factory():
    """Создать generic метод фабрики (совместимость)"""
    return CSharpMethodFactory.create_generic_factory_method()

def create_validation_method():
    """Создать метод валидации (совместимость)"""
    return CSharpMethodFactory.create_validation_method()

def create_simple_method():
    """Создать простой метод (совместимость)"""
    return CSharpMethodFactory.create_simple_method()

# Удобные функции для C# кода (совместимость)
def create_user_factory_code():
    """Создать код метода фабрики пользователя (совместимость)"""
    return CSharpCodeFactory.create_user_factory_code()

def create_message_factory_code():
    """Создать код метода фабрики сообщения (совместимость)"""
    return CSharpCodeFactory.create_message_factory_code()

def create_generic_factory_code():
    """Создать код generic метода фабрики (совместимость)"""
    return CSharpCodeFactory.create_generic_factory_code()

def create_simple_method_code():
    """Создать код простого метода (совместимость)"""
    return CSharpCodeFactory.create_simple_method_code()

def create_testkit_class_code():
    """Создать код класса TestKit (совместимость)"""
    return CSharpCodeFactory.create_testkit_class_code()

__all__ = [
    # Telegram/User factories
    'UserFactory',
    'MessageFactory',
    'user_factory',
    'message_factory',
    'create_user',
    'create_message',
    'create_telegram_user',
    'create_telegram_message',
    'create_command_message',
    'create_bot_message',
    
    # C# factories
    'CSharpMethodFactory',
    'CSharpCodeFactory',
    'csharp_method_factory',
    'csharp_code_factory',
    'create_user_factory',
    'create_message_factory',
    'create_generic_factory',
    'create_validation_method',
    'create_simple_method',
    'create_user_factory_code',
    'create_message_factory_code',
    'create_generic_factory_code',
    'create_simple_method_code',
    'create_testkit_class_code'
]
