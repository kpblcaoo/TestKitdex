# TestKitdex Project Workflow

## 🎯 Быстрый старт

### 1. Понимание задачи
- **BDD-first**: Всегда начинай с BDD сценария в `features/`
- **TDD цикл**: Сценарий → Тест → Код → Рефакторинг
- **Планы**: Проверяй `plans/` для архитектуры и метрик

### 2. Структура проекта
```
src/                    # Основной код
├── testkit_indexer/    # Парсинг C# → SQLite
├── mcp_server/         # FastAPI для AI ассистентов
└── cli/               # Командная строка

tests/                  # Тесты
├── unit/              # Компоненты
├── integration/       # API
└── acceptance/        # E2E

features/              # BDD сценарии (8 файлов)
data/testkit_sample/   # TestKit инфра (как в ClubDoorman)
```

### 3. Рабочий процесс

#### Новая фича:
1. **BDD**: `features/new_feature.feature` (@tag)
2. **Unit**: `tests/unit/test_new_feature.py`
3. **Code**: `src/module/new_feature.py`
4. **Integration**: `tests/integration/test_new_feature_api.py`

#### Исправление бага:
1. **Reproduce**: BDD сценарий с edge case
2. **Fix**: Минимальное изменение
3. **Test**: Все тесты проходят
4. **Document**: Обновить планы если нужно

### 4. Ключевые принципы

#### Архитектура:
- **SQLite-first**: Быстрый поиск, FTS5
- **MCP API**: FastAPI для AI интеграции
- **BDD-TDD**: 90%+ покрытие тестами
- **Performance**: < 100мс поиск, < 30с индексация

#### Код:
- **Type hints**: 100% типизация
- **Docstrings**: Все публичные методы
- **Error handling**: RFC 7807 формат
- **Logging**: DEBUG для разработки

### 5. Команды для проверки

```bash
# Тесты
pytest tests/ -v
behave features/ --tags=@feature_name

# Качество
black --check .
flake8 .
mypy src/

# Производительность
python -m src.cli.main index /path/to/testkit
python -m src.cli.main search "query"
```

### 6. Метрики успеха

#### Качество:
- Покрытие: > 90%
- Линтинг: 0 ошибок
- Типизация: 100%

#### Производительность:
- Индексация: < 30 сек (1000 методов)
- Поиск: < 100мс
- API: < 200мс

#### Полезность:
- Точность поиска: > 85%
- AI подсказки: > 80%

### 7. Частые задачи

#### Добавить новый тег:
1. `features/tag_hierarchy.feature` - сценарий
2. `src/testkit_indexer/tag_extractor.py` - логика
3. `tests/unit/test_tag_extractor.py` - тест

#### Улучшить поиск:
1. `features/search.feature` - edge case
2. `src/testkit_indexer/search.py` - алгоритм
3. `tests/unit/test_search.py` - производительность

#### Добавить API endpoint:
1. `features/mcp_api.feature` - сценарий
2. `src/mcp_server/handlers.py` - обработчик
3. `tests/integration/test_mcp_server.py` - тест

### 8. Полезные ссылки

- **Планы**: `plans/ARCHITECTURE_PLAN.md`
- **BDD**: `features/` (8 сценариев)
- **TestKit**: `data/testkit_sample/`
- **Документация**: `docs/DEVELOPMENT.md`

---

**Правило**: Всегда начинай с BDD сценария, следуй TDD циклу, проверяй метрики качества и производительности. 