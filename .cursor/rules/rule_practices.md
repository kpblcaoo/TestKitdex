# TestKitdex Testing Practices

## 🎯 Общие принципы тестирования

### BDD-TDD подход
- **BDD first**: Начинай с Gherkin сценариев в `features/`
- **TDD cycle**: Gherkin → Step Definitions → Unit Tests → Code → Green
- **Покрытие**: > 90% для unit тестов, > 80% для BDD сценариев

### Структура тестов
```
tests/
├── unit/              # Unit тесты компонентов
├── integration/       # Integration тесты API
├── acceptance/        # BDD step definitions
└── factories/         # Test data factories

features/
├── *.feature         # Gherkin сценарии
├── steps/           # Step definitions
└── environment.py   # Setup/teardown
```

## 📋 Правила написания тестов

### 1. Unit тесты (`tests/unit/`)

#### Структура unit теста:
```python
"""
Unit tests for [module_name] functionality.
"""
import pytest
from src.module.component import Component
from tests.factories import create_test_data


class TestComponent:
    """Test [Component] functionality."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.component = Component()
    
    def test_specific_functionality(self):
        """Test specific functionality."""
        # Given
        test_data = create_test_data()
        
        # When
        result = self.component.process(test_data)
        
        # Then
        assert result is not None
        assert result.property == expected_value
```

#### Правила:
- ✅ **Один тест = одна функциональность**
- ✅ **Given-When-Then структура**
- ✅ **Используй factories для test data**
- ✅ **Покрытие > 95%**
- ❌ **НЕ тестируй private методы**
- ❌ **НЕ делай тесты зависимыми друг от друга**

### 2. BDD тесты (`features/`)

#### Gherkin сценарии:
```gherkin
@feature_name
Feature: [Feature Name]
  As a [user type]
  I want to [action]
  So that [benefit]

  Scenario: [Scenario name]
    Given [precondition]
    When [action]
    Then [expected result]
```

#### Step definitions:
```python
"""
Step definitions for [feature] scenarios.
"""
from behave import given, when, then
from tests.unit.test_component import TestComponent


@given("I have [condition]")
def step_impl(context):
    """Create [condition] for testing."""
    # Use existing unit test setup
    context.test_component = TestComponent()
    context.test_component.setup_method()
    
    # Create test data
    context.test_data = create_test_data()


@when("I [action]")
def step_impl(context):
    """Perform [action]."""
    # Use existing unit test with our data
    if hasattr(context, 'test_data'):
        result = context.test_component.process(context.test_data)
        context.result = result


@then("it should [expected]")
def step_impl(context):
    """Verify [expected]."""
    # Use existing unit test assertion with our data
    if hasattr(context, 'result'):
        assert context.result.property == expected_value
```

#### Правила:
- ✅ **Step definitions = тонкий слой** между Gherkin и unit тестами
- ✅ **Передавай данные** через `context`
- ✅ **Используй существующие unit тесты** для проверок
- ✅ **Создавай test data** в Given шагах
- ❌ **НЕ дублируй бизнес-логику** в step definitions
- ❌ **НЕ создавай сложную логику** в step definitions

### 3. Test Factories (`tests/factories/`)

#### Структура factory:
```python
"""
Test data factories for [module].
"""
from src.module.models import Model


def create_test_model(**kwargs):
    """Create test model with default values."""
    defaults = {
        "name": "TestModel",
        "value": "test_value",
        "tags": ["test", "factory"]
    }
    defaults.update(kwargs)
    
    return Model(**defaults)


def create_test_data():
    """Create test data for specific scenario."""
    return {
        "models": [create_test_model() for _ in range(3)],
        "metadata": {"version": "1.0"}
    }
```

#### Правила:
- ✅ **Используй разумные defaults**
- ✅ **Поддерживай override через kwargs**
- ✅ **Создавай разные factories для разных сценариев**
- ✅ **Документируй назначение каждой factory**
- ❌ **НЕ создавай слишком сложные объекты**
- ❌ **НЕ делай factories зависимыми друг от друга**

### 4. Integration тесты (`tests/integration/`)

#### Структура integration теста:
```python
"""
Integration tests for [API/Service].
"""
import pytest
from fastapi.testclient import TestClient
from src.api.main import app


class TestAPI:
    """Test API endpoints."""
    
    def setup_method(self):
        """Set up test client."""
        self.client = TestClient(app)
    
    def test_endpoint_functionality(self):
        """Test specific endpoint."""
        # Given
        test_data = {"key": "value"}
        
        # When
        response = self.client.post("/api/endpoint", json=test_data)
        
        # Then
        assert response.status_code == 200
        assert response.json()["result"] == "success"
```

#### Правила:
- ✅ **Тестируй реальные API endpoints**
- ✅ **Используй TestClient для FastAPI**
- ✅ **Проверяй HTTP status codes**
- ✅ **Валидируй response format**
- ❌ **НЕ тестируй внутреннюю логику** (это для unit тестов)
- ❌ **НЕ делай тесты медленными**

## 🔄 TDD цикл разработки

### 1. Новая фича:
```bash
# 1. Создай BDD сценарий
vim features/new_feature.feature

# 2. Создай step definitions
vim features/steps/new_feature_steps.py

# 3. Напиши unit тесты
vim tests/unit/test_new_feature.py

# 4. Реализуй код
vim src/module/new_feature.py

# 5. Запусти тесты
pytest tests/unit/test_new_feature.py
behave features/new_feature.feature
```

### 2. Исправление бага:
```bash
# 1. Создай BDD сценарий с edge case
vim features/bug_fix.feature

# 2. Напиши unit тест который падает
vim tests/unit/test_bug_fix.py

# 3. Исправь код
vim src/module/buggy_code.py

# 4. Убедись что все тесты проходят
pytest && behave
```

## 📊 Метрики качества

### Покрытие тестами:
- **Unit тесты**: > 95%
- **Integration тесты**: > 90%
- **BDD сценарии**: > 80%
- **Acceptance тесты**: > 85%

### Производительность:
- **Unit тесты**: < 1 сек на тест
- **Integration тесты**: < 5 сек на тест
- **BDD тесты**: < 10 сек на сценарий
- **Полный test suite**: < 2 минуты

### Качество кода:
- **Linting**: 0 ошибок
- **Type checking**: 100% типизировано
- **Documentation**: 100% публичных методов
- **Code review**: Все тесты проходят review

## 🛠 Команды для тестирования

### Запуск тестов:
```bash
# Unit тесты
pytest tests/unit/ -v

# Integration тесты
pytest tests/integration/ -v

# BDD тесты
behave features/ --tags=@feature_name

# Все тесты
pytest && behave

# С покрытием
pytest --cov=src tests/
```

### Отладка тестов:
```bash
# Запуск с отладкой
pytest -s tests/unit/test_specific.py

# BDD с подробным выводом
behave features/ --verbose

# Показать невыполненные шаги
behave --dry-run features/
```

## 🎯 Лучшие практики

### 1. Именование:
- ✅ **Тесты**: `test_what_it_tests`
- ✅ **Factories**: `create_what_it_creates`
- ✅ **Scenarios**: Описательные названия
- ✅ **Steps**: Понятные Given-When-Then

### 2. Организация:
- ✅ **Группируй связанные тесты** в классы
- ✅ **Используй setup/teardown** для фикстур
- ✅ **Разделяй unit/integration/BDD** тесты
- ✅ **Документируй сложные тесты**

### 3. Поддержка:
- ✅ **Рефактори тесты** вместе с кодом
- ✅ **Обновляй тесты** при изменении API
- ✅ **Удаляй устаревшие тесты**
- ✅ **Мониторь производительность** тестов

### 4. Отладка:
- ✅ **Используй assert messages** для понятных ошибок
- ✅ **Логируй промежуточные результаты**
- ✅ **Создавай минимальные воспроизводимые тесты**
- ✅ **Используй debugger для сложных случаев**

## 🚨 Анти-паттерны

### ❌ НЕ делай:
- **Тесты зависимыми** друг от друга
- **Сложную логику** в step definitions
- **Тестирование private методов**
- **Медленные тесты** без необходимости
- **Дублирование test data**
- **Игнорирование падающих тестов**

### ✅ Делай:
- **Изолированные тесты**
- **Простые step definitions**
- **Тестирование публичного API**
- **Быстрые тесты**
- **Переиспользование factories**
- **Немедленное исправление падающих тестов**

---

**Помни**: Хорошие тесты - это инвестиция в будущее проекта. Они экономят время на отладку и дают уверенность в изменениях. 