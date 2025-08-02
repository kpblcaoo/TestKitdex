# ADR-002: Migration from Custom Factories to Factory Boy

## Status
Proposed

## Context
В проекте используются кастомные factory классы для создания тестовых данных:
- `CSharpMethodFactory` в `tests/factories/csharp_method_factory.py`
- `CSharpCodeFactory` в `tests/factories/csharp_code_factory.py`

Эти кастомные factories работают, но не используют возможности factory-boy:
- Нет автоматической генерации данных
- Нет SubFactory для связанных объектов
- Нет интеграции с pytest fixtures
- Сложно переиспользовать в разных тестах

## Decision
Мигрировать с кастомных factories на factory-boy:

### Migration Strategy
1. **Постепенная миграция** - не ломать существующие тесты
2. **Создать новые factory-boy factories** параллельно
3. **Обновить тесты** для использования factory-boy
4. **Удалить кастомные factories** после полной миграции

### New Factory Structure
```python
# tests/factories/csharp_method_factory.py
from factory import Factory, Faker, SubFactory
from src.testkit_indexer.parser.models import CSharpMethod

class CSharpMethodFactory(Factory):
    class Meta:
        model = CSharpMethod
    
    name = Faker('word')
    return_type = Faker('random_element', elements=['void', 'string', 'int', 'bool'])
    parameters = []
    tags = []
    summary = Faker('sentence')
    is_static = Faker('boolean')
    is_generic = Faker('boolean')
    is_public = True
    file_path = Faker('file_path', depth=2)
    line_number = Faker('random_int', min=1, max=1000)
```

### Benefits
- Автоматическая генерация реалистичных данных
- Легкое создание связанных объектов
- Интеграция с pytest fixtures
- Лучшая читаемость тестов

## Consequences

### Positive
- Более мощные возможности генерации данных
- Лучшая интеграция с pytest
- Меньше boilerplate кода
- Стандартный подход

### Negative
- Время на миграцию
- Временная сложность поддержки двух подходов
- Обучение команды factory-boy

### Neutral
- Сохранение функциональности
- Улучшение качества тестов

## Implementation Plan
1. Создать factory-boy версии существующих factories
2. Обновить unit тесты для использования factory-boy
3. Обновить BDD step definitions
4. Удалить кастомные factories
5. Обновить документацию

## References
- [factory-boy documentation](https://factoryboy.readthedocs.io/)
- [pytest-factoryboy documentation](https://pytest-factoryboy.readthedocs.io/) 