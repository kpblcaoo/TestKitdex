"""
Простой DI контейнер для тестов
Аналог DI из C# TestKit
"""

from typing import Any, Dict, Type, TypeVar, Optional, Callable
from dataclasses import dataclass
import inspect

T = TypeVar('T')

class TestContainer:
    """Простой DI контейнер для тестов"""
    
    def __init__(self):
        self._services: Dict[Type, Any] = {}
        self._factories: Dict[Type, Callable] = {}
        self._singletons: Dict[Type, Any] = {}
    
    def register(self, service_type: Type[T], implementation: T) -> None:
        """Зарегистрировать сервис"""
        self._services[service_type] = implementation
    
    def register_factory(self, service_type: Type[T], factory: Callable[[], T]) -> None:
        """Зарегистрировать фабрику"""
        self._factories[service_type] = factory
    
    def register_singleton(self, service_type: Type[T], implementation: T) -> None:
        """Зарегистрировать синглтон"""
        self._singletons[service_type] = implementation
    
    def resolve(self, service_type: Type[T]) -> T:
        """Получить сервис"""
        # Проверяем синглтоны
        if service_type in self._singletons:
            return self._singletons[service_type]
        
        # Проверяем обычные сервисы
        if service_type in self._services:
            return self._services[service_type]
        
        # Проверяем фабрики
        if service_type in self._factories:
            return self._factories[service_type]()
        
        # Пытаемся создать автоматически
        return self._auto_create(service_type)
    
    def _auto_create(self, service_type: Type[T]) -> T:
        """Автоматическое создание объекта"""
        try:
            # Пробуем создать без параметров
            return service_type()
        except TypeError:
            # Если нужны параметры, создаём моки
            sig = inspect.signature(service_type.__init__)
            kwargs = {}
            
            for param_name, param in sig.parameters.items():
                if param_name == 'self':
                    continue
                
                if param.annotation != inspect.Parameter.empty:
                    # Создаём мок для параметра
                    kwargs[param_name] = self._create_mock(param.annotation)
                elif param.default != inspect.Parameter.empty:
                    kwargs[param_name] = param.default
                else:
                    kwargs[param_name] = None
            
            return service_type(**kwargs)
    
    def _create_mock(self, mock_type: Type) -> Any:
        """Создать мок объект"""
        if mock_type == str:
            return "mock_string"
        elif mock_type == int:
            return 0
        elif mock_type == bool:
            return False
        elif mock_type == list:
            return []
        elif mock_type == dict:
            return {}
        else:
            # Создаём простой мок объект
            return type(f"Mock{mock_type.__name__}", (), {})()
    
    def clear(self) -> None:
        """Очистить контейнер"""
        self._services.clear()
        self._factories.clear()
        self._singletons.clear()

# Глобальный контейнер
container = TestContainer()

# Удобные функции
def register(service_type: Type[T], implementation: T) -> None:
    """Зарегистрировать сервис"""
    container.register(service_type, implementation)

def resolve(service_type: Type[T]) -> T:
    """Получить сервис"""
    return container.resolve(service_type)

def create_mock(service_type: Type[T]) -> T:
    """Создать мок сервиса"""
    return container._create_mock(service_type)

# Экспорт
__all__ = ['TestContainer', 'container', 'register', 'resolve', 'create_mock'] 