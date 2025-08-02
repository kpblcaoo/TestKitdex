# BDD Builders для TestKit

## Обзор

BDD Builders предоставляют универсальный Fluent API для создания тестовых данных в BDD сценариях. Они интегрируются с существующими фабриками и поддерживают параметризованные шаги.

## Архитектура

```
┌─────────────────────────────────────┐
│           BDD Builders              │  ← Fluent API для BDD
├─────────────────────────────────────┤
│           Factories                 │  ← Бизнес-логика создания
├─────────────────────────────────────┤
│           Models                    │  ← Данные (CSharpMethod)
└─────────────────────────────────────┘
```

## Основные компоненты

### 1. BDDDataBuilder

Универсальный билдер для создания тестовых данных в BDD сценариях.

```python
from data.testkit_sample.builders import create_bdd_data

# Создание данных для сценария поиска
search_data = (create_bdd_data()
    .for_search_scenario()
    .build())

# Создание данных для сценария анализа тегов
tag_analysis_data = (create_bdd_data()
    .for_tag_analysis_scenario()
    .build())

# Создание сложного сценария
complex_data = (create_bdd_data()
    .with_clean_database()
    .with_indexed_methods(100)
    .with_search_index()
    .with_test_data()
    .with_tag_hierarchy()
    .with_ai_capabilities()
    .build())
```

### 2. CSharpMethodBuilder

Fluent API для создания C# методов.

```python
from data.testkit_sample.builders import create_method_builder

# Создание метода напрямую
method = (create_method_builder()
    .with_name("CustomMethod")
    .with_return_type("string")
    .with_tags("custom", "test")
    .with_parameters("int id", "string name")
    .static()
    .build())

# Создание метода через фабрику
factory_method = (create_method_builder()
    .as_user_factory()
    .build())
```

### 3. CSharpCodeBuilder

Fluent API для создания C# кода.

```python
from data.testkit_sample.builders import create_code_builder

# Создание кода напрямую
code = (create_code_builder()
    .with_method_name("TestMethod")
    .with_return_type("void")
    .with_tags("test", "example")
    .with_summary("Test method for demonstration")
    .static()
    .build())

# Создание кода через фабрику
factory_code = (create_code_builder()
    .as_user_factory_code()
    .build())
```

## Готовые сценарии

### for_search_scenario()
Создает данные для сценариев поиска:
- Чистая база данных
- 100 индексированных методов
- Поисковый индекс
- Тестовые данные с различными тегами

### for_tag_analysis_scenario()
Создает данные для сценариев анализа тегов:
- Чистая база данных
- 50 индексированных методов
- Иерархия тегов
- AI возможности

### for_indexing_scenario()
Создает данные для сценариев индексации:
- Чистая база данных
- Тестовые данные
- XML документация
- Сложные сигнатуры

### for_performance_scenario()
Создает данные для сценариев производительности:
- Чистая база данных
- 1000 методов
- Поисковый индекс

### for_error_scenario()
Создает данные для сценариев обработки ошибок:
- Чистая база данных
- Файлы с ошибками
- Конфликтующие теги

## Параметризованные шаги

BDD Builders поддерживают параметризованные шаги для унификации BDD сценариев:

```python
# features/steps/common_steps.py
@given("I have {data_type} with {condition}")
def step_impl(context, data_type, condition):
    bdd_builder = create_bdd_data()
    
    if data_type == "a clean database":
        context.test_data = bdd_builder.with_clean_database().build()
    elif data_type == "10000 indexed methods":
        context.test_data = bdd_builder.with_large_dataset(10000).build()
    # ... другие условия

@when("I run {command}")
def step_impl(context, command):
    if command == "the indexer":
        # Симулируем индексацию
        context.indexed_methods = len(context.test_data.methods)
    elif command == '"tkx diff old.db new.db"':
        # Симулируем diff
        context.diff_result = {"added": 5, "modified": 2, "deleted": 1}
    # ... другие команды

@then("I should get {result_type}")
def step_impl(context, result_type):
    if result_type == "an error with code 400":
        assert hasattr(context, 'error_code') and context.error_code == 400
    elif result_type == "methods tagged with both":
        assert hasattr(context, 'search_results') and len(context.search_results) > 0
    # ... другие результаты
```

## Интеграция с фабриками

BDD Builders опираются на существующие фабрики:

```python
# Использование фабрики через билдер
method = (create_method_builder()
    .as_user_factory()  # Использует CSharpMethodFactory.create_user_factory_method()
    .build())

# Переопределение параметров
method = (create_method_builder()
    .as_user_factory()
    .with_name("CustomUserFactory")  # Переопределяем имя
    .build())
```

## Преимущества

1. **Универсальность** - один API для всех типов тестовых данных
2. **Интеграция** - работает с существующими фабриками
3. **Читаемость** - Fluent API для понятного кода
4. **Параметризация** - поддержка параметризованных BDD шагов
5. **Готовые сценарии** - предопределенные конфигурации для типовых случаев

## Использование в BDD

```gherkin
Feature: TestKit Search
  Background:
    Given I have a clean database
    And I have indexed TestKit methods
    And the search index is built
    And I have test data with various tags and methods

  Scenario: Search by tags
    When I search for tags "message" and "factory"
    Then I should get methods tagged with both
    And results should be sorted by relevance_score DESC
    And the first result should have relevance_score >= 0.8
    And I should see method details
```

## Примеры

См. `data/testkit_sample/examples/bdd_example.py` для полных примеров использования.

## Зависимости

- `factory-boy` - для интеграции с фабриками
- `parse` - для параметризованных шагов
- `behave` - для BDD сценариев 