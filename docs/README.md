# TestKitdex Documentation

## Overview
TestKitdex - система индексации и поиска TestKit компонентов с поддержкой C# парсинга.

## Architecture Decision Records (ADR)

### ADR-001: Testing Tools and Framework Selection
[ADR_001_TESTING_TOOLS.md](./ADR_001_TESTING_TOOLS.md)
- Выбор инструментов тестирования
- Factory-boy, pytest, behave
- Инструменты для производительности и покрытия

### ADR-002: Migration from Custom Factories to Factory Boy
[ADR_002_FACTORY_PATTERN_MIGRATION.md](./ADR_002_FACTORY_PATTERN_MIGRATION.md)
- План миграции с кастомных factories
- Стратегия постепенной миграции
- Улучшение качества тестовых данных

### ADR-003: TestKit Optimization and Act Integration
[ADR_003_TESTKIT_OPTIMIZATION.md](./ADR_003_TESTKIT_OPTIMIZATION.md)
- Оптимизация TestKit с factory-boy
- Интеграция с Act для локального тестирования GitHub Actions
- Улучшенная структура тестовых данных

### ADR-004: Test Migration to Optimized TestKit
[ADR_004_TEST_MIGRATION_TO_TESTKIT.md](./ADR_004_TEST_MIGRATION_TO_TESTKIT.md)
- Миграция тестов на новый TestKit с factory-boy
- Обратная совместимость с существующими тестами
- Улучшение качества тестовых данных

## Development Documentation

### Development Guide
[DEVELOPMENT.md](./DEVELOPMENT.md)
- Руководство по разработке
- Настройка окружения
- Процесс разработки

## Project Structure

```
docs/
├── README.md                           # Этот файл
├── ADR_001_TESTING_TOOLS.md           # ADR по инструментам тестирования
├── ADR_002_FACTORY_PATTERN_MIGRATION.md # ADR по миграции factories
├── ADR_003_TESTKIT_OPTIMIZATION.md    # ADR по оптимизации TestKit
├── ADR_004_TEST_MIGRATION_TO_TESTKIT.md # ADR по миграции тестов
└── DEVELOPMENT.md                      # Руководство по разработке
```

## Quick Start

1. Установить зависимости: `pip install -r requirements.txt`
2. Настроить базу данных: `alembic upgrade head`
3. Запустить тесты: `pytest`
4. Запустить BDD тесты: `behave`
5. Тестировать GitHub Actions локально: `./scripts/test_with_act.sh`

## Testing Strategy

- **Unit Tests**: pytest + factory-boy ✅
- **BDD Tests**: behave + Gherkin ✅
- **Performance**: pytest-benchmark ✅
- **Coverage**: pytest-cov ✅
- **Parallel Execution**: pytest-xdist ✅
- **Local GitHub Actions**: Act ✅

## TestKit Optimization

### Factory Integration
```python
from data.testkit_sample.factories import create_user, create_message
from data.testkit_sample.generators import create_simple_scenario

# Создание тестовых данных
user = create_user()
message = create_message()
scenario = create_simple_scenario()
```

### Act Integration
```bash
# Локальное тестирование GitHub Actions
./scripts/test_with_act.sh

# С реальными данными
./scripts/test_with_act.sh --with-data
```

## Enhanced TestKit Structure

```
data/testkit_sample/
├── factories/           # Factory-boy factories
│   ├── user_factory.py
│   ├── message_factory.py
│   ├── csharp_factories.py
│   ├── code_factories.py
│   └── __init__.py
├── generators/          # Генераторы сценариев
│   ├── scenario_generator.py
│   └── __init__.py
├── builders/           # Fluent API builders
├── services/           # Сервисные билдеры
├── infra/              # Инфраструктура
├── scenarios/          # Готовые сценарии
├── golden_master/      # Golden Master тесты
├── mocks/              # Моки
└── fixtures/           # Тестовые данные
```

## Migration Results

### ✅ Completed
- **26/29 unit tests passed** (3 skipped for future implementation)
- **Factory-boy integration** - мощная генерация тестовых данных
- **Backward compatibility** - старые тесты работают
- **Enhanced TestKit structure** - улучшенная организация
- **Act integration** - локальное тестирование CI/CD

### 🔄 In Progress
- Парсер тегов (2 теста пропущены)
- Статистика базы данных (1 тест пропущен)
- FTS5 поиск (1 тест пропущен)

### 📈 Benefits Achieved
- Единообразный подход к тестовым данным
- Автоматическая генерация с Faker
- Лучшая читаемость и поддерживаемость тестов
- Интеграция с современными инструментами тестирования 