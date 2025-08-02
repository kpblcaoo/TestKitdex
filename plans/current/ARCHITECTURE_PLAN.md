# TestKit Infrastructure - План архитектуры

## 🎯 Цель проекта

Создать интеллектуальную инфраструктуру для индексации и поиска TestKit компонентов с поддержкой:
- SQLite-first подхода для быстрого поиска
- MCP API для интеграции с AI ассистентами
- AI-подсказок тегов и методов
- BDD-TDD подхода к разработке

## 🏗️ Архитектурные принципы

### 1. SQLite-first подход
- **Быстрая индексация**: SQLite для хранения метаданных
- **Гибкий поиск**: SQL запросы с JOIN'ами
- **FTS5**: Полнотекстовый поиск по описаниям
- **Индексы**: Оптимизация по тегам, категориям, return-type

### 2. MCP API поверх SQLite
- **FastAPI сервер**: REST API для MCP интеграции
- **Асинхронность**: Поддержка множественных запросов
- **Кэширование**: Redis для частых запросов
- **Валидация**: Pydantic модели

### 3. BDD-TDD подход
- **Features**: Gherkin сценарии для поведения
- **Unit тесты**: Покрытие каждого компонента
- **Integration тесты**: Тестирование API
- **Acceptance тесты**: End-to-end сценарии

## 📁 Структура проекта

```
testkit-infrastructure/
├── README.md
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── features/                    # BDD сценарии
│   ├── indexing.feature
│   ├── search.feature
│   ├── mcp_api.feature
│   └── suggestions.feature
├── src/
│   ├── testkit_indexer/         # Основная логика
│   │   ├── __init__.py
│   │   ├── indexer.py           # Главный класс индексации
│   │   ├── database/            # SQLite слой
│   │   │   ├── __init__.py
│   │   │   ├── models.py        # Pydantic модели
│   │   │   ├── migrations.py    # Миграции БД
│   │   │   └── queries.py       # SQL запросы
│   │   ├── parser/              # Парсинг C#
│   │   │   ├── __init__.py
│   │   │   ├── csharp_parser.py # Парсер C# файлов
│   │   │   └── tag_extractor.py # Извлечение тегов
│   │   └── utils.py             # Утилиты
│   ├── mcp_server/              # MCP API
│   │   ├── __init__.py
│   │   ├── server.py            # FastAPI сервер
│   │   ├── handlers.py          # Обработчики запросов
│   │   ├── models.py            # API модели
│   │   └── middleware.py        # Middleware
│   └── cli/                     # Командная строка
│       ├── __init__.py
│       ├── main.py              # Точка входа CLI
│       └── commands.py          # Команды
├── tests/
│   ├── unit/                    # Unit тесты
│   │   ├── test_parser.py
│   │   ├── test_indexer.py
│   │   └── test_database.py
│   ├── integration/             # Integration тесты
│   │   ├── test_mcp_server.py
│   │   └── test_search_api.py
│   └── acceptance/              # Acceptance тесты
│       ├── test_indexing_workflow.py
│       └── test_search_workflow.py
├── data/                        # Тестовые данные
│   ├── testkit_sample/          # Пример TestKit
│   └── fixtures/                # Фикстуры для тестов
├── docs/                        # Документация
│   ├── architecture.md
│   ├── api.md
│   └── deployment.md
└── plans/                       # Планы разработки
    ├── ARCHITECTURE_PLAN.md
    ├── DEVELOPMENT_PLAN.md
    └── DEPLOYMENT_PLAN.md
```

## 🗄️ База данных (SQLite)

### Схема БД

```sql
-- Компоненты (файлы/классы)
CREATE TABLE components (
    id INTEGER PRIMARY KEY,
    file_path TEXT NOT NULL,
    class_name TEXT,
    category TEXT,
    description TEXT,
    lines_count INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Методы
CREATE TABLE methods (
    id INTEGER PRIMARY KEY,
    component_id INTEGER,
    name TEXT NOT NULL,
    return_type TEXT,
    signature TEXT,
    description TEXT,
    line_number INTEGER,
    is_static BOOLEAN,
    is_generic BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (component_id) REFERENCES components(id)
);

-- Теги
CREATE TABLE tags (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    category TEXT,
    description TEXT,
    usage_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Связь методы-теги
CREATE TABLE method_tags (
    method_id INTEGER,
    tag_id INTEGER,
    PRIMARY KEY (method_id, tag_id),
    FOREIGN KEY (method_id) REFERENCES methods(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);

-- FTS5 для полнотекстового поиска
CREATE VIRTUAL TABLE methods_fts USING fts5(
    name, description, signature, 
    content='methods', content_rowid='id'
);

-- Индексы для быстрого поиска
CREATE INDEX idx_methods_name ON methods(name);
CREATE INDEX idx_methods_return_type ON methods(return_type);
CREATE INDEX idx_tags_name ON tags(name);
CREATE INDEX idx_tags_category ON tags(category);
CREATE INDEX idx_components_category ON components(category);
```

## 🔌 MCP API

### Endpoints

```python
# Основные endpoints
GET /methods                    # Список методов с фильтрацией
GET /methods/{id}               # Детали метода
GET /components                 # Список компонентов
GET /components/{id}            # Детали компонента
GET /tags                       # Список тегов
GET /search                     # Поиск по всем критериям

# AI endpoints
POST /suggest/tags              # AI подсказки тегов
POST /suggest/methods           # AI подсказки методов
POST /analyze/context           # Анализ контекста

# Управление
POST /index                     # Индексация TestKit
DELETE /index                   # Очистка индекса
GET /stats                      # Статистика
```

### Модели данных

```python
from pydantic import BaseModel
from typing import List, Optional

class Method(BaseModel):
    id: int
    name: str
    return_type: str
    signature: str
    description: Optional[str]
    tags: List[str]
    component: str
    line_number: int
    is_static: bool
    is_generic: bool

class SearchRequest(BaseModel):
    tags: Optional[List[str]] = None
    category: Optional[str] = None
    query: Optional[str] = None
    return_type: Optional[str] = None
    limit: int = 20
    offset: int = 0

class TagSuggestion(BaseModel):
    tag: str
    confidence: float
    reason: str

class ContextAnalysis(BaseModel):
    context: str
    suggested_tags: List[TagSuggestion]
    suggested_methods: List[Method]
    confidence: float
```

## 🧪 BDD сценарии

### indexing.feature
```gherkin
Feature: TestKit Indexing
  As a developer
  I want to index TestKit components
  So that I can search and discover test utilities

  Scenario: Index C# files with tags
    Given I have a TestKit directory with C# files
    When I run the indexer
    Then it should parse all .cs files
    And extract methods with their tags
    And store them in SQLite database
    And create indexes for fast search

  Scenario: Handle complex tag hierarchies
    Given I have methods with multiple tags
    When I index the methods
    Then it should normalize tag names
    And create tag relationships
    And support tag inheritance
```

### search.feature
```gherkin
Feature: Advanced Search
  As a developer
  I want to search TestKit methods
  So that I can find relevant utilities quickly

  Scenario: Search by tags
    Given I have indexed TestKit methods
    When I search for tags "message" and "factory"
    Then I should get methods tagged with both
    And results should be ranked by relevance

  Scenario: Semantic search
    Given I have indexed TestKit with descriptions
    When I search for "create user message"
    Then I should get methods for creating user messages
    And results should include semantic matches
```

## 🔄 TDD циклы разработки

### Цикл 1: Базовая индексация (1-2 недели)
1. ✅ Feature: Parse C# files
2. ✅ Test: Extract methods and tags
3. ✅ Implementation: CSharpParser
4. ✅ Test: Database storage
5. ✅ Implementation: SQLite storage

### Цикл 2: Поиск (1-2 недели)
1. ✅ Feature: Search by tags
2. ✅ Test: Tag-based queries
3. ✅ Implementation: Search engine
4. ✅ Test: FTS5 integration
5. ✅ Implementation: Full-text search

### Цикл 3: MCP API (1-2 недели)
1. ✅ Feature: MCP server
2. ✅ Test: API endpoints
3. ✅ Implementation: FastAPI server
4. ✅ Test: MCP protocol
5. ✅ Implementation: MCP handlers

### Цикл 4: AI Integration (2-3 недели)
1. ✅ Feature: Tag suggestions
2. ✅ Test: Context analysis
3. ✅ Implementation: AI tagger
4. ✅ Test: Semantic search
5. ✅ Implementation: Embeddings

## 🛠️ Технологический стек

### Backend
- **Python 3.11+**: Основной язык
- **FastAPI**: Web framework для MCP API
- **SQLite**: База данных
- **Pydantic**: Валидация данных
- **Alembic**: Миграции БД

### Testing
- **pytest**: Unit и integration тесты
- **behave**: BDD тесты
- **factory-boy**: Фабрики для тестов
- **pytest-asyncio**: Асинхронные тесты

### Development
- **black**: Форматирование кода
- **flake8**: Линтинг
- **mypy**: Типизация
- **pre-commit**: Git hooks

### AI/ML (будущее)
- **sentence-transformers**: Эмбеддинги
- **scikit-learn**: Классификация
- **numpy/pandas**: Обработка данных

## 📊 Метрики успеха

### Производительность
- Индексация: < 30 сек для 1000 методов
- Поиск: < 100мс для простых запросов
- API: < 200мс для MCP запросов

### Качество
- Покрытие тестами: > 90%
- BDD сценарии: > 80% покрытие
- Документация: 100% API endpoints

### Полезность
- Точность поиска: > 85%
- Релевантность AI подсказок: > 80%
- Время поиска методов: < 30 сек

## 🔍 Diff-движок

### Концепция
Сравнение двух состояний TestKit для отслеживания изменений:
- Добавленные/удаленные методы
- Новые теги и их использование
- Изменения в line_number (рефакторинг)
- CI/CD интеграция

### CLI команда
```bash
tkx diff old.db new.db --output diff.md
```

### Схема сравнения
```sql
-- Таблица для отслеживания изменений
CREATE TABLE method_changes (
    id INTEGER PRIMARY KEY,
    method_id INTEGER,
    change_type TEXT, -- 'added', 'removed', 'modified'
    old_signature TEXT,
    new_signature TEXT,
    old_tags TEXT,
    new_tags TEXT,
    old_line_number INTEGER,
    new_line_number INTEGER,
    diff_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (method_id) REFERENCES methods(id)
);

-- Индексы для быстрого сравнения
CREATE INDEX idx_method_changes_type ON method_changes(change_type);
CREATE INDEX idx_method_changes_timestamp ON method_changes(diff_timestamp);
```

### API endpoints
```python
# Diff API
GET /diff/{old_version}/{new_version}     # Получить diff между версиями
POST /diff/compare                         # Сравнить два состояния
GET /diff/summary                          # Сводка изменений
```

### BDD сценарий
```gherkin
Feature: TestKit Diff
  As a developer
  I want to see changes in TestKit
  So that I can track evolution and impact

  Scenario: Compare two TestKit states
    Given I have two TestKit databases: old.db and new.db
    When I run "tkx diff old.db new.db"
    Then I should see added methods
    And I should see removed methods
    And I should see modified method signatures
    And I should see new tags
    And the output should be in markdown format
```

## 📈 Отчеты и аналитика

### Концепция
Генерация аналитических отчетов для понимания состояния TestKit:
- Топ используемых тегов
- Неиспользуемые методы
- Coverage по доменам
- Тренды использования

### CLI команды
```bash
tkx report usage --output reports/usage.md
tkx report coverage --output reports/coverage.md
tkx report trends --output reports/trends.md
```

### Схема отчетов
```sql
-- Таблица для метрик использования
CREATE TABLE usage_metrics (
    id INTEGER PRIMARY KEY,
    tag_name TEXT,
    usage_count INTEGER,
    last_used TIMESTAMP,
    trend_direction TEXT, -- 'up', 'down', 'stable'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица для coverage метрик
CREATE TABLE coverage_metrics (
    id INTEGER PRIMARY KEY,
    domain TEXT,
    total_methods INTEGER,
    used_methods INTEGER,
    coverage_percentage REAL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### API endpoints
```python
# Reports API
GET /reports/usage                    # Топ тегов и методов
GET /reports/coverage                 # Coverage по доменам
GET /reports/trends                   # Тренды использования
GET /reports/unused                   # Неиспользуемые методы
```

### BDD сценарий
```gherkin
Feature: TestKit Reports
  As a team lead
  I want to see TestKit usage reports
  So that I can optimize test utilities

  Scenario: Generate usage report
    Given I have indexed TestKit with usage data
    When I run "tkx report usage"
    Then I should see top 10 used tags
    And I should see unused methods
    And I should see coverage by domain
    And the report should be in markdown format
```

## 🏷️ Тег-граф и иерархия

### Концепция
Иерархическая система тегов для улучшения поиска и AI-подсказок:
- Родительские и дочерние теги
- Наследование свойств
- Семантические связи
- Улучшенные AI-подсказки

### Схема тег-графа
```sql
-- Иерархия тегов
CREATE TABLE tag_relations (
    parent_tag TEXT,
    child_tag TEXT,
    relation_type TEXT, -- 'is_a', 'has_a', 'related_to'
    confidence REAL DEFAULT 1.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (parent_tag, child_tag),
    FOREIGN KEY (parent_tag) REFERENCES tags(name),
    FOREIGN KEY (child_tag) REFERENCES tags(name)
);

-- Индексы для быстрого поиска по иерархии
CREATE INDEX idx_tag_relations_parent ON tag_relations(parent_tag);
CREATE INDEX idx_tag_relations_child ON tag_relations(child_tag);
CREATE INDEX idx_tag_relations_type ON tag_relations(relation_type);
```

### Примеры иерархии
```sql
-- Иерархия тегов
INSERT INTO tag_relations VALUES
('moderation', 'ban', 'is_a', 1.0),
('moderation', 'warn', 'is_a', 1.0),
('user', 'registration', 'has_a', 1.0),
('user', 'profile', 'has_a', 1.0),
('message', 'telegram', 'related_to', 0.8),
('message', 'discord', 'related_to', 0.8);
```

### API endpoints
```python
# Tag Graph API
GET /tags/hierarchy                    # Получить иерархию тегов
GET /tags/{tag}/children              # Дочерние теги
GET /tags/{tag}/parents               # Родительские теги
GET /tags/{tag}/related               # Связанные теги
POST /tags/analyze                    # AI анализ связей
```

### BDD сценарий
```gherkin
Feature: Tag Hierarchy
  As a developer
  I want to use hierarchical tags
  So that I can find related methods easily

  Scenario: Search with tag inheritance
    Given I have a tag hierarchy with "moderation" as parent
    And "ban" and "warn" are child tags of "moderation"
    When I search for methods with tag "moderation"
    Then I should get methods tagged with "moderation"
    And I should get methods tagged with "ban"
    And I should get methods tagged with "warn"
    And results should be ranked by relevance
```

## 🚀 Следующие шаги

1. **Настройка окружения**: Создание базовой структуры
2. **Первый TDD цикл**: Базовая индексация
3. **BDD сценарии**: Определение поведения
4. **Прототип**: Минимальная рабочая версия
5. **Интеграция**: Тестирование с реальным TestKit 