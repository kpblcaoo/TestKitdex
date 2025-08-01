# TestKit Infrastructure - План разработки

## 🎯 Цели разработки

Создать TestKit инфраструктуру используя BDD-TDD подход с фокусом на:
- **Качество кода**: 90%+ покрытие тестами
- **Поведение**: BDD сценарии для всех фич
- **Производительность**: Быстрый поиск и индексация
- **Интеграция**: MCP API для AI ассистентов

## 🔄 TDD циклы разработки

### Цикл 1: Базовая индексация (1-2 недели)

#### Неделя 1: Парсинг C# файлов

**День 1-2: Настройка проекта** ✅ ЗАВЕРШЕНО
- [x] Создание базовой структуры
- [x] Настройка pytest + behave
- [x] Первые BDD сценарии
- [x] Создание CSharpParser с полным покрытием тестами
- [x] Модели данных CSharpMethod и ParseResult
- [x] Поддержка XML документации и тегов
- [x] Обработка generic методов

**День 3-4: Парсер C#** ✅ ЗАВЕРШЕНО
- [x] Базовый парсер с поддержкой тегов
- [x] Обработка сложных случаев
- [x] Обработка ошибок
- [x] Логирование
- [x] Интеграция с файловой системой
- [x] TestKit фабрики для тестов
- [x] 18 тестов с полным покрытием

**День 5: Интеграция парсера**
- [ ] Обработка сложных случаев
- [ ] Обработка ошибок
- [ ] Логирование

#### Неделя 2: База данных

**День 1-2: SQLite схема**
```python
# tests/unit/test_database.py
def test_store_method_with_tags():
    # Given
    method = Method(name="CreateMessage", tags=["message", "factory"])
    
    # When
    db.store_method(method)
    
    # Then
    stored = db.get_method_by_name("CreateMessage")
    assert stored.tags == ["message", "factory"]
```

**День 3-4: Миграции и индексы**
- [ ] Alembic миграции
- [ ] Создание индексов
- [ ] FTS5 настройка

**День 5: Интеграция**
- [ ] End-to-end тесты
- [ ] Производительность
- [ ] Документация

### Цикл 2: Поиск (1-2 недели)

#### Неделя 1: Базовый поиск

**День 1-2: Поиск по тегам**
```python
# tests/unit/test_search.py
def test_search_by_tags():
    # Given
    db.add_method(method1, tags=["message", "factory"])
    db.add_method(method2, tags=["user", "factory"])
    
    # When
    results = db.search_by_tags(["message", "factory"])
    
    # Then
    assert len(results) == 1
    assert results[0].name == "CreateMessage"
```

**День 3-4: FTS5 поиск**
- [ ] Полнотекстовый поиск
- [ ] Ранжирование результатов
- [ ] Фильтрация

**День 5: Оптимизация**
- [ ] Индексы для быстрого поиска
- [ ] Кэширование результатов
- [ ] Профилирование

#### Неделя 2: Продвинутый поиск

**День 1-2: Комбинированный поиск**
- [ ] Поиск по тегам + текст
- [ ] Поиск по return type
- [ ] Поиск по категориям

**День 3-4: Ранжирование**
- [ ] Алгоритм релевантности
- [ ] Веса для разных критериев
- [ ] A/B тестирование

**День 5: API для поиска**
- [ ] REST endpoints
- [ ] Валидация запросов
- [ ] Документация API

### Цикл 3: MCP API (1-2 недели)

#### Неделя 1: FastAPI сервер

**День 1-2: Базовая структура**
```python
# tests/integration/test_mcp_server.py
def test_search_endpoint():
    # Given
    server = MCPServer()
    
    # When
    response = server.search(tags=["message", "factory"])
    
    # Then
    assert response.status_code == 200
    assert "methods" in response.json()
```

**День 3-4: Основные endpoints**
- [ ] GET /methods
- [ ] GET /components
- [ ] GET /tags
- [ ] GET /search

**День 5: Валидация и ошибки**
- [ ] Pydantic модели
- [ ] Обработка ошибок
- [ ] Логирование

#### Неделя 2: MCP интеграция

**День 1-2: MCP протокол**
- [ ] MCP handlers
- [ ] Асинхронные запросы
- [ ] Кэширование

**День 3-4: AI интеграция**
- [ ] Контекстный поиск
- [ ] Подсказки методов
- [ ] Семантический анализ

**День 5: Тестирование и документация**
- [ ] Integration тесты
- [ ] API документация
- [ ] Примеры использования

### Цикл 4: AI Integration (2-3 недели)

#### Неделя 1: Базовые AI фичи

**День 1-2: Tag suggestions**
```python
# tests/unit/test_ai_suggestions.py
def test_suggest_tags_for_context():
    # Given
    context = "I need to create a test user with a message"
    
    # When
    suggestions = ai_suggester.suggest_tags(context)
    
    # Then
    assert "user" in suggestions
    assert "message" in suggestions
    assert suggestions[0].confidence > 0.8
```

**День 3-4: Embeddings**
- [ ] Sentence transformers
- [ ] Векторизация методов
- [ ] Семантический поиск

**День 5: Интеграция с БД**
- [ ] Хранение эмбеддингов
- [ ] Индексы для векторов
- [ ] Производительность

#### Неделя 2: Продвинутые AI фичи

**День 1-2: Контекстный анализ**
- [ ] Анализ кода
- [ ] Понимание намерений
- [ ] Рекомендации

**День 3-4: Машинное обучение**
- [ ] Классификация методов
- [ ] Предсказание использования
- [ ] Персонализация

**День 5: Оптимизация**
- [ ] Кэширование AI результатов
- [ ] Batch processing
- [ ] Мониторинг качества

#### Неделя 3: Интеграция и тестирование

**День 1-2: End-to-end тесты**
- [ ] Полные сценарии использования
- [ ] Производительность
- [ ] Нагрузочное тестирование

**День 3-4: Документация**
- [ ] API документация
- [ ] Примеры использования
- [ ] Руководство по развертыванию

**День 5: Финальная подготовка**
- [ ] Исправление багов
- [ ] Оптимизация
- [ ] Подготовка к релизу

### Цикл 5: Diff-движок (1-2 недели)

#### Неделя 1: Базовая функциональность

**День 1-2: Сравнение методов**
```python
# tests/unit/test_diff.py
def test_compare_methods():
    # Given
    old_methods = [Method(name="CreateUser", tags=["user", "factory"])]
    new_methods = [Method(name="CreateUser", tags=["user", "factory", "validation"])]
    
    # When
    diff = diff_engine.compare_methods(old_methods, new_methods)
    
    # Then
    assert len(diff.added_tags) == 1
    assert "validation" in diff.added_tags
    assert diff.modified_methods[0].name == "CreateUser"
```

**День 3-4: CLI команда**
- [ ] `tkx diff old.db new.db` команда
- [ ] Markdown вывод
- [ ] Детализация изменений

**День 5: API endpoints**
- [ ] GET /diff/{old}/{new}
- [ ] POST /diff/compare
- [ ] Валидация входных данных

#### Неделя 2: Интеграция и отчеты

**День 1-2: CI/CD интеграция**
- [ ] GitHub Actions workflow
- [ ] Автоматическая генерация diff.md
- [ ] Комментарии в PR

**День 3-4: Детализация**
- [ ] Изменения line_number
- [ ] Анализ рефакторинга
- [ ] Статистика изменений

**День 5: Тестирование**
- [ ] Integration тесты
- [ ] Performance тесты
- [ ] Документация

### Цикл 6: Отчеты и аналитика (1-2 недели)

#### Неделя 1: Базовые отчеты

**День 1-2: Usage отчеты**
```python
# tests/unit/test_reports.py
def test_generate_usage_report():
    # Given
    db.add_method(method1, usage_count=10)
    db.add_method(method2, usage_count=5)
    
    # When
    report = report_generator.usage_report()
    
    # Then
    assert report.top_tags[0].name == "message"
    assert report.top_tags[0].usage_count == 10
    assert len(report.unused_methods) > 0
```

**День 3-4: Coverage отчеты**
- [ ] Coverage по доменам
- [ ] Неиспользуемые методы
- [ ] Тренды использования

**День 5: CLI команды**
- [ ] `tkx report usage`
- [ ] `tkx report coverage`
- [ ] `tkx report trends`

#### Неделя 2: Продвинутая аналитика

**День 1-2: Метрики качества**
- [ ] Качество тегов
- [ ] Дублирование методов
- [ ] Сложность методов

**День 3-4: Визуализация**
- [ ] Графики трендов
- [ ] Heatmaps использования
- [ ] Интерактивные отчеты

**День 5: Интеграция**
- [ ] Автоматические отчеты
- [ ] Уведомления
- [ ] Экспорт данных

### Цикл 7: Тег-граф и иерархия (1-2 недели)

#### Неделя 1: Базовая иерархия

**День 1-2: Схема тег-графа**
```python
# tests/unit/test_tag_graph.py
def test_tag_hierarchy():
    # Given
    graph.add_relation("moderation", "ban", "is_a")
    graph.add_relation("moderation", "warn", "is_a")
    
    # When
    children = graph.get_children("moderation")
    
    # Then
    assert "ban" in children
    assert "warn" in children
    assert len(children) == 2
```

**День 3-4: Поиск с наследованием**
- [ ] Поиск по родительским тегам
- [ ] Автоматическое включение дочерних
- [ ] Ранжирование по релевантности

**День 5: API endpoints**
- [ ] GET /tags/hierarchy
- [ ] GET /tags/{tag}/children
- [ ] GET /tags/{tag}/parents

#### Неделя 2: AI интеграция

**День 1-2: AI анализ связей**
- [ ] Автоматическое определение связей
- [ ] Предложение иерархии
- [ ] Confidence scoring

**День 3-4: Улучшенные подсказки**
- [ ] Контекстные подсказки
- [ ] Семантический поиск
- [ ] Персонализация

**День 5: Оптимизация**
- [ ] Кэширование графа
- [ ] Индексы для быстрого поиска
- [ ] Performance tuning

## 🧪 BDD сценарии

BDD сценарии определены в папке `features/`:

- **@indexing** - `features/indexing.feature` - Индексация TestKit компонентов
- **@search** - `features/search.feature` - Продвинутый поиск
- **@mcp_api** - `features/mcp_api.feature` - MCP API интеграция
- **@suggestions** - `features/suggestions.feature` - AI подсказки
- **@diff** - `features/diff.feature` - Diff-движок
- **@reports** - `features/reports.feature` - Отчеты и аналитика
- **@tag_hierarchy** - `features/tag_hierarchy.feature` - Ручная иерархия тегов
- **@tag_analysis** - `features/tag_analysis.feature` - AI анализ тегов

### Запуск тестов по тегам
```bash
# Запуск всех тестов
behave features/

# Запуск тестов по тегам
behave --tags=@indexing
behave --tags=@search
behave --tags=@mcp_api
behave --tags=@suggestions
behave --tags=@diff
behave --tags=@reports
behave --tags=@tag_hierarchy
behave --tags=@tag_analysis
```

## 🧪 Метрики качества

### Покрытие тестами
- **Unit тесты**: > 95%
- **Integration тесты**: > 90%
- **BDD сценарии**: > 80%
- **Acceptance тесты**: > 85%

### Производительность
- **Индексация**: < 30 сек для 1000 методов
- **Поиск**: < 100мс для простых запросов
- **API**: < 200мс для MCP запросов
- **AI suggestions**: < 500мс

### Качество кода
- **Linting**: 0 ошибок
- **Type checking**: 100% типизировано
- **Documentation**: 100% API endpoints
- **Code review**: Все PR проходят review

### Дополнительные метрики

#### Diff-движок
- **Скорость сравнения**: < 5 сек для 1000 методов
- **Точность diff**: 100% обнаружение изменений
- **CI интеграция**: Автоматические отчеты в PR

#### Отчеты
- **Генерация отчетов**: < 10 сек для полного отчета
- **Актуальность данных**: < 1 час отставания
- **Полезность**: > 80% actionable insights

#### Тег-граф
- **Поиск по иерархии**: < 50мс
- **AI точность**: > 85% правильных связей
- **Автоматизация**: > 70% связей определяются автоматически

## 🚀 Критерии готовности

### MVP (Цикл 1-2)
- [ ] Базовая индексация работает
- [ ] Поиск по тегам работает
- [ ] CLI интерфейс готов
- [ ] Базовые тесты проходят

### Beta (Цикл 3)
- [ ] MCP API работает
- [ ] Интеграция с AI ассистентами
- [ ] Документация готова
- [ ] Performance тесты проходят

### Release (Цикл 4)
- [ ] AI подсказки работают
- [ ] Все BDD сценарии проходят
- [ ] Production ready
- [ ] Мониторинг настроен

### Advanced Features (Циклы 5-7)
- [ ] Diff-движок работает
- [ ] Отчеты генерируются автоматически
- [ ] Тег-иерархия улучшает поиск
- [ ] CI/CD интеграция настроена
- [ ] AI подсказки используют иерархию

## 📝 Ежедневные задачи

### Утренний ритуал
1. **Проверить тесты**: `pytest && behave`
2. **Проверить линтинг**: `flake8 && black --check`
3. **Обновить план**: Что сделано, что в процессе
4. **Выбрать задачу**: Следующий TDD цикл

### Вечерний ритуал
1. **Запустить все тесты**: Убедиться что ничего не сломалось
2. **Обновить документацию**: Если добавил новую функциональность
3. **Коммит изменений**: С осмысленными сообщениями
4. **Планирование завтра**: Следующие шаги

## 🔄 Итерации

### Итерация 1 (Недели 1-2): Foundation
- Базовая структура проекта
- Парсинг C# файлов
- SQLite интеграция
- Первые тесты

### Итерация 2 (Недели 3-4): Search
- Поиск по тегам
- FTS5 интеграция
- CLI интерфейс
- Performance оптимизация

### Итерация 3 (Недели 5-6): API
- FastAPI сервер
- MCP интеграция
- REST endpoints
- Документация API

### Итерация 4 (Недели 7-9): AI
- Tag suggestions
- Semantic search
- Embeddings
- ML интеграция

### Итерация 5 (Недели 10-11): Polish
- End-to-end тесты
- Performance tuning
- Documentation
- Production readiness 

### Итерация 6 (Недели 12-13): Diff & Reports
- Diff-движок
- Отчеты и аналитика
- CI/CD интеграция
- Автоматизация

### Итерация 7 (Недели 14-15): Tag Graph
- Иерархия тегов
- AI анализ связей
- Улучшенный поиск
- Персонализация 