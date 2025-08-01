# TestKitdex

Intelligent TestKit indexing and search infrastructure with MCP API integration.

## 🎯 Цель проекта

Создать интеллектуальную инфраструктуру для индексации и поиска TestKit компонентов с поддержкой:
- SQLite-first подхода для быстрого поиска
- MCP API для интеграции с AI ассистентами
- AI-подсказок тегов и методов
- BDD-TDD подхода к разработке

## 🏗️ Архитектура

### SQLite-first подход
- **Быстрая индексация**: SQLite для хранения метаданных
- **Гибкий поиск**: SQL запросы с JOIN'ами
- **FTS5**: Полнотекстовый поиск по описаниям
- **Индексы**: Оптимизация по тегам, категориям, return-type

### MCP API поверх SQLite
- **FastAPI сервер**: REST API для MCP интеграции
- **Асинхронность**: Поддержка множественных запросов
- **Кэширование**: Redis для частых запросов
- **Валидация**: Pydantic модели

### BDD-TDD подход
- **Features**: Gherkin сценарии для поведения
- **Unit тесты**: Покрытие каждого компонента
- **Integration тесты**: Тестирование API
- **Acceptance тесты**: End-to-end сценарии

## 📁 Структура проекта

```
testkit-infrastructure/
├── src/
│   ├── testkit_indexer/         # Основная логика
│   ├── mcp_server/              # MCP API
│   └── cli/                     # Командная строка
├── tests/
│   ├── unit/                    # Unit тесты
│   ├── integration/             # Integration тесты
│   └── acceptance/              # Acceptance тесты
├── features/                    # BDD сценарии
├── data/
│   └── testkit_sample/          # Тестовые данные
├── docs/                        # Документация
└── plans/                       # Планы разработки
```

## 🚀 Быстрый старт

```bash
# Клонирование
git clone https://github.com/your-username/TestKitdex.git
cd TestKitdex

# Установка зависимостей
pip install -r requirements.txt

# Запуск индексации
python -m src.cli.main index /path/to/testkit

# Запуск поиска
python -m src.cli.main search "message factory"

# Запуск MCP сервера
python -m src.mcp_server.main
```

## 🧪 BDD сценарии

Проект использует BDD-TDD подход с полным покрытием сценариев:

```bash
# Запуск всех тестов
behave features/

# Запуск по тегам
behave --tags=@indexing
behave --tags=@search
behave --tags=@mcp_api
behave --tags=@suggestions
behave --tags=@diff
behave --tags=@reports
behave --tags=@tag_hierarchy
behave --tags=@tag_analysis
```

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

## 🔧 Технологический стек

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

## 📝 Планы разработки

- **[ARCHITECTURE_PLAN.md](plans/ARCHITECTURE_PLAN.md)** - План архитектуры
- **[DEVELOPMENT_PLAN.md](plans/DEVELOPMENT_PLAN.md)** - План разработки
- **[READINESS_STATUS.md](plans/READINESS_STATUS.md)** - Статус готовности

## 🤝 Вклад в проект

1. Fork репозитория
2. Создайте feature branch (`git checkout -b feature/amazing-feature`)
3. Commit изменения (`git commit -m 'Add amazing feature'`)
4. Push в branch (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📄 Лицензия

MIT License - см. [LICENSE](LICENSE) файл для деталей.

## 🆘 Поддержка

Если у вас есть вопросы или проблемы:
- Создайте [Issue](https://github.com/your-username/TestKitdex/issues)
- Обратитесь к [документации](docs/)
- Проверьте [планы разработки](plans/)

---

**TestKitdex** - Интеллектуальная инфраструктура для индексации и поиска TestKit компонентов 🚀 