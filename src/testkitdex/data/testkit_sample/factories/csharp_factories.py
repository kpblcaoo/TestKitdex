"""
C# Factories using factory-boy
"""

from factory import Factory, Faker, SubFactory
from typing import Dict, Any, List
from src.testkit_indexer.parser.models import CSharpMethod


class CSharpMethodFactory(Factory):
    """Factory for creating C# methods using factory-boy"""
    
    class Meta:
        model = CSharpMethod
    
    name = Faker('word')
    return_type = Faker('random_element', elements=['void', 'string', 'int', 'bool', 'User', 'Message', 'T'])
    parameters = []
    tags = []
    summary = Faker('sentence')
    is_static = Faker('boolean')
    is_generic = Faker('boolean')
    is_public = True
    file_path = Faker('file_path', depth=2)
    line_number = Faker('random_int', min=1, max=1000)
    
    @classmethod
    def create_user_factory_method(cls) -> CSharpMethod:
        """Создать метод фабрики пользователя"""
        return cls.create(
            name="CreateUser",
            return_type="User",
            parameters=["string name = \"TestUser\""],
            tags=["user", "factory", "test-data"],
            summary="Creates a test user",
            is_static=True,
            is_public=True
        )
    
    @classmethod
    def create_message_factory_method(cls) -> CSharpMethod:
        """Создать метод фабрики сообщения"""
        return cls.create(
            name="CreateMessage",
            return_type="Message",
            parameters=["string text = \"Test message\""],
            tags=["message", "factory", "telegram"],
            summary="Creates a test message",
            is_static=True,
            is_public=True
        )
    
    @classmethod
    def create_generic_factory_method(cls) -> CSharpMethod:
        """Создать generic метод фабрики"""
        return cls.create(
            name="CreateFactory",
            return_type="T",
            parameters=[],
            tags=["factory", "generic"],
            summary="Generic factory method",
            is_static=True,
            is_generic=True,
            is_public=True
        )
    
    @classmethod
    def create_validation_method(cls) -> CSharpMethod:
        """Создать метод валидации"""
        return cls.create(
            name="ValidateUser",
            return_type="bool",
            parameters=["User user"],
            tags=["validation", "user"],
            summary="Validates user data",
            is_static=False,
            is_public=True
        )
    
    @classmethod
    def create_simple_method(cls) -> CSharpMethod:
        """Создать простой метод без тегов"""
        return cls.create(
            name="DoSomething",
            return_type="void",
            parameters=[],
            tags=[],
            summary="Simple method without tags",
            is_static=False,
            is_public=True
        )
    
    @classmethod
    def create_complex_method(cls) -> CSharpMethod:
        """Создать сложный метод с параметрами"""
        return cls.create(
            name="ProcessData",
            return_type="string",
            parameters=["int id", "string name", "bool active = true"],
            tags=["processing", "data"],
            summary="Processes data with multiple parameters",
            is_static=False,
            is_public=True
        )


# Удобные функции для обратной совместимости
def create_user_factory() -> CSharpMethod:
    """Создать метод фабрики пользователя (совместимость)"""
    return CSharpMethodFactory.create_user_factory_method()

def create_message_factory() -> CSharpMethod:
    """Создать метод фабрики сообщения (совместимость)"""
    return CSharpMethodFactory.create_message_factory_method()

def create_generic_factory() -> CSharpMethod:
    """Создать generic метод фабрики (совместимость)"""
    return CSharpMethodFactory.create_generic_factory_method()

def create_validation_method() -> CSharpMethod:
    """Создать метод валидации (совместимость)"""
    return CSharpMethodFactory.create_validation_method()

def create_simple_method() -> CSharpMethod:
    """Создать простой метод (совместимость)"""
    return CSharpMethodFactory.create_simple_method() 