# ADR-004: Test Migration to Optimized TestKit

## Status
Proposed

## Context
Существующие тесты используют кастомные factories в `tests/factories/`:
- `test_factories.py` - тестирует кастомные CSharpMethodFactory
- `test_parser.py` - использует кастомные code factories
- `test_database.py` - использует кастомные method factories

Нужно мигрировать на новый TestKit с factory-boy для:
- Единообразия подхода к тестовым данным
- Использования возможностей factory-boy
- Улучшения читаемости и поддерживаемости тестов

## Decision
Мигрировать тесты на новый TestKit с factory-boy:

### 1. Migration Strategy

#### Phase 1: Create TestKit Factories for C# Models
```python
# data/testkit_sample/factories/csharp_factories.py
from factory import Factory, Faker, SubFactory
from src.testkit_indexer.parser.models import CSharpMethod

class CSharpMethodFactory(Factory):
    class Meta:
        model = CSharpMethod
    
    name = Faker('word')
    return_type = Faker('random_element', elements=['void', 'string', 'int', 'bool', 'User', 'Message'])
    parameters = []
    tags = []
    summary = Faker('sentence')
    is_static = Faker('boolean')
    is_generic = Faker('boolean')
    is_public = True
    file_path = Faker('file_path', depth=2)
    line_number = Faker('random_int', min=1, max=1000)
    
    @classmethod
    def create_user_factory_method(cls):
        return cls.create(
            name="CreateUser",
            return_type="User",
            parameters=["string name = \"TestUser\""],
            tags=["user", "factory", "test-data"],
            summary="Creates a test user",
            is_static=True
        )
    
    @classmethod
    def create_message_factory_method(cls):
        return cls.create(
            name="CreateMessage", 
            return_type="Message",
            parameters=["string text = \"Test message\""],
            tags=["message", "factory", "telegram"],
            summary="Creates a test message",
            is_static=True
        )
```

#### Phase 2: Update Test Files
```python
# tests/unit/test_factories.py
from data.testkit_sample.factories.csharp_factories import CSharpMethodFactory

class TestCSharpMethodFactory:
    def test_create_user_factory_method(self):
        # When
        method = CSharpMethodFactory.create_user_factory_method()
        
        # Then
        assert method.name == "CreateUser"
        assert method.return_type == "User"
        assert method.tags == ["user", "factory", "test-data"]
```

#### Phase 3: Create TestKit Integration
```python
# data/testkit_sample/testkit_integration.py
from .factories.csharp_factories import CSharpMethodFactory
from .generators.scenario_generator import TestScenarioGenerator

class TestKitIntegration:
    """Интеграция TestKit с существующими тестами"""
    
    @staticmethod
    def create_parser_test_scenario():
        """Создать сценарий для тестирования парсера"""
        return {
            "methods": [
                CSharpMethodFactory.create_user_factory_method(),
                CSharpMethodFactory.create_message_factory_method(),
                CSharpMethodFactory.create_generic_factory_method()
            ],
            "metadata": {
                "scenario_type": "parser_test",
                "description": "Сценарий для тестирования C# парсера"
            }
        }
```

### 2. Backward Compatibility
```python
# tests/factories/__init__.py - ОБНОВИТЬ
# Импортировать из нового TestKit для обратной совместимости
from data.testkit_sample.factories.csharp_factories import (
    CSharpMethodFactory,
    create_user_factory_method as create_user_factory,
    create_message_factory_method as create_message_factory
)
```

### 3. Enhanced Test Structure
```
tests/
├── unit/
│   ├── test_factories.py      # Обновить на factory-boy
│   ├── test_parser.py         # Обновить на TestKit
│   └── test_database.py       # Обновить на TestKit
├── integration/
│   └── test_parser_integration.py
└── factories/                 # УДАЛИТЬ после миграции
```

## Consequences

### Positive
- Единообразный подход к тестовым данным
- Мощные возможности factory-boy
- Лучшая читаемость тестов
- Автоматическая генерация данных

### Negative
- Время на миграцию
- Временная сложность поддержки двух подходов
- Обучение команды новому API

### Neutral
- Сохранение функциональности тестов
- Улучшение качества тестовых данных

## Implementation Plan

### Phase 1: Create TestKit C# Factories
1. Создать `data/testkit_sample/factories/csharp_factories.py`
2. Создать `data/testkit_sample/factories/code_factories.py`
3. Обновить `data/testkit_sample/factories/__init__.py`

### Phase 2: Update Test Files
1. Обновить `tests/unit/test_factories.py`
2. Обновить `tests/unit/test_parser.py`
3. Обновить `tests/unit/test_database.py`

### Phase 3: Create Integration Layer
1. Создать `data/testkit_sample/testkit_integration.py`
2. Обновить `tests/factories/__init__.py` для совместимости
3. Добавить тесты для нового TestKit

### Phase 4: Cleanup
1. Удалить старые кастомные factories
2. Обновить документацию
3. Добавить примеры использования

## References
- [factory-boy documentation](https://factoryboy.readthedocs.io/)
- [pytest-factoryboy documentation](https://pytest-factoryboy.readthedocs.io/)
- [ADR-002: Factory Pattern Migration](./ADR_002_FACTORY_PATTERN_MIGRATION.md) 