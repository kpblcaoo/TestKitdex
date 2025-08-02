# ADR-001: Testing Tools and Framework Selection

## Status
Accepted

## Context
Проект TestKitdex требует надежной системы тестирования с поддержкой:
- Unit тестов для парсера C# кода
- BDD тестов для интеграционных сценариев  
- Factory pattern для создания тестовых данных
- Измерения покрытия кода
- Параллельного выполнения тестов
- Бенчмаркинга производительности

## Decision
Выбраны следующие инструменты тестирования:

### Core Testing Framework
- **pytest** - основной фреймворк для unit тестов
- **behave** - для BDD тестов с Gherkin

### Test Data Management
- **factory-boy** - для создания тестовых данных через factories
- **Faker** - для генерации реалистичных тестовых данных
- **pytest-factoryboy** - интеграция factory-boy с pytest

### Test Execution & Performance
- **pytest-xdist** - параллельное выполнение unit тестов
- **behave-parallel** - параллельное выполнение BDD тестов
- **pytest-benchmark** - бенчмаркинг производительности

### Code Quality & Coverage
- **pytest-cov** - измерение покрытия кода
- **pytest-mock** - моки и стабы (встроен в pytest)

### Code Quality Tools
- **black** - форматирование кода
- **flake8** - линтинг
- **mypy** - статическая типизация
- **pre-commit** - pre-commit хуки

## Consequences

### Positive
- Единообразный подход к тестированию
- Высокая производительность тестов
- Хорошее покрытие кода
- Автоматизация качества кода

### Negative
- Дополнительные зависимости
- Сложность настройки CI/CD
- Обучение команды новым инструментам

### Neutral
- Миграция с кастомных factories на factory-boy
- Обновление существующих тестов

## Implementation Plan
1. Обновить requirements.txt
2. Мигрировать кастомные factories на factory-boy
3. Настроить pytest.ini для всех инструментов
4. Добавить pre-commit конфигурацию
5. Обновить CI/CD pipeline

## References
- [factory-boy documentation](https://factoryboy.readthedocs.io/)
- [pytest documentation](https://docs.pytest.org/)
- [behave documentation](https://behave.readthedocs.io/) 