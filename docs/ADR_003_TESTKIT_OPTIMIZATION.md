# ADR-003: TestKit Optimization and Act Integration

## Status
Proposed

## Context
Текущий TestKit имеет базовую функциональность, но нуждается в оптимизации:
- Простые генераторы данных
- Нет интеграции с factory-boy
- Нет поддержки Act для локального тестирования GitHub Actions
- Отсутствует структурированный подход к тестовым данным

## Decision
Оптимизировать TestKit и интегрировать Act:

### 1. TestKit Optimization

#### Factory Integration
```python
# data/testkit_sample/factories/__init__.py
from factory import Factory, Faker, SubFactory
from .user_factory import UserFactory
from .message_factory import MessageFactory

# Глобальные factories
user_factory = UserFactory()
message_factory = MessageFactory()
```

#### Structured Data Generation
```python
# data/testkit_sample/generators.py
class TestDataGenerator:
    def __init__(self):
        self.faker = Faker()
    
    def create_testkit_scenario(self, complexity: str = "simple"):
        """Создать полный тестовый сценарий"""
        return {
            "users": [user_factory() for _ in range(3)],
            "messages": [message_factory() for _ in range(5)],
            "metadata": {
                "scenario_type": complexity,
                "created_at": self.faker.date_time()
            }
        }
```

### 2. Act Integration

#### GitHub Actions Testing
```yaml
# .github/workflows/test.yml
name: Test with Act
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: |
          python -m pytest
          behave features/
```

#### Local Act Testing
```bash
# scripts/test_with_act.sh
#!/bin/bash
# Локальное тестирование GitHub Actions

echo "Testing GitHub Actions locally with Act..."

# Тестируем push workflow
act push --dry-run

# Тестируем pull_request workflow  
act pull_request --dry-run

# Тестируем с реальными данными
act push --artifact-server-path /tmp/artifacts
```

### 3. Enhanced TestKit Structure

```
data/testkit_sample/
├── __init__.py              # Основной TestKit
├── factories/               # Factory-boy factories
│   ├── __init__.py
│   ├── user_factory.py
│   ├── message_factory.py
│   └── chat_factory.py
├── generators/              # Генераторы сценариев
│   ├── __init__.py
│   ├── scenario_generator.py
│   └── data_generator.py
├── act_integration/         # Act интеграция
│   ├── __init__.py
│   ├── workflow_tester.py
│   └── local_runner.py
├── builders/               # Fluent API builders
├── services/               # Сервисные билдеры
├── infra/                  # Инфраструктура
├── scenarios/              # Готовые сценарии
├── golden_master/          # Golden Master тесты
├── mocks/                  # Моки
└── fixtures/               # Тестовые данные
```

## Consequences

### Positive
- Мощная генерация тестовых данных через factory-boy
- Локальное тестирование GitHub Actions
- Структурированный подход к тестам
- Лучшая интеграция с CI/CD

### Negative
- Сложность настройки Act
- Дополнительные зависимости
- Время на миграцию

### Neutral
- Сохранение обратной совместимости
- Постепенная миграция

## Implementation Plan

### Phase 1: Factory Integration
1. Создать factory-boy factories
2. Интегрировать с существующим TestKit
3. Обновить генераторы данных

### Phase 2: Act Integration  
1. Настроить GitHub Actions workflows
2. Создать Act тестирование
3. Добавить локальные скрипты

### Phase 3: Enhanced Structure
1. Реорганизовать структуру TestKit
2. Создать генераторы сценариев
3. Добавить документацию

## References
- [Act documentation](https://nektosact.com/)
- [factory-boy documentation](https://factoryboy.readthedocs.io/)
- [GitHub Actions](https://docs.github.com/en/actions) 