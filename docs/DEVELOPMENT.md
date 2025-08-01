# Development Guide - TestKitdex

## 🚀 Быстрый старт

### Установка окружения

```bash
# Клонирование репозитория
git clone https://github.com/your-username/TestKitdex.git
cd TestKitdex

# Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows

# Установка зависимостей
pip install -r requirements.txt

# Установка pre-commit hooks
pre-commit install
```

### Первый запуск

```bash
# Проверка установки
python -c "from data.testkit_sample import TK; print('TestKit loaded:', TK.create_user())"

# Запуск тестов
pytest tests/
behave features/

# Проверка линтинга
black --check .
flake8 .
mypy .
```

## 🏗️ Архитектура проекта

### Структура папок

```
TestKitdex/
├── src/                          # Основной код
│   ├── testkit_indexer/          # Индексация TestKit
│   ├── mcp_server/               # MCP API сервер
│   └── cli/                      # Командная строка
├── tests/                        # Тесты
│   ├── unit/                     # Unit тесты
│   ├── integration/              # Integration тесты
│   └── acceptance/               # Acceptance тесты
├── features/                     # BDD сценарии
├── data/testkit_sample/          # TestKit инфра
├── docs/                         # Документация
└── plans/                        # Планы разработки
```

### Основные компоненты

1. **testkit_indexer** - Парсинг и индексация C# файлов
2. **mcp_server** - FastAPI сервер для MCP интеграции
3. **cli** - Командная строка для индексации и поиска
4. **TestKit инфра** - Удобные генераторы для тестов

## 🧪 Тестирование

### BDD сценарии

```bash
# Запуск всех BDD тестов
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

### Unit тесты

```bash
# Запуск всех unit тестов
pytest tests/unit/

# Запуск с покрытием
pytest --cov=src tests/unit/

# Запуск по маркерам
pytest -m "fast"
pytest -m "slow"
```

### Integration тесты

```bash
# Запуск integration тестов
pytest tests/integration/

# Тестирование API
pytest tests/integration/test_mcp_server.py
```

## 🔧 Разработка

### TDD циклы

Проект следует BDD-TDD подходу:

1. **BDD сценарий** - Описываем поведение
2. **Unit тест** - Тестируем компонент
3. **Реализация** - Пишем код
4. **Refactoring** - Улучшаем код

### Создание новой фичи

```bash
# 1. Создаём BDD сценарий
touch features/new_feature.feature

# 2. Пишем unit тесты
touch tests/unit/test_new_feature.py

# 3. Реализуем функциональность
touch src/testkit_indexer/new_feature.py

# 4. Добавляем integration тесты
touch tests/integration/test_new_feature_api.py
```

### Code Style

```bash
# Форматирование кода
black src/ tests/

# Линтинг
flake8 src/ tests/

# Типизация
mypy src/

# Проверка всех стилей
pre-commit run --all-files
```

## 📊 Метрики качества

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

## 🛠️ Инструменты разработки

### Pre-commit hooks

```bash
# Установка hooks
pre-commit install

# Запуск на всех файлах
pre-commit run --all-files

# Запуск конкретного hook
pre-commit run black
pre-commit run flake8
```

### Отладка

```bash
# Запуск с отладкой
python -m pdb -m src.cli.main

# Логирование
export LOG_LEVEL=DEBUG
python -m src.cli.main

# Профилирование
python -m cProfile -o profile.stats src/cli/main.py
```

### Тестирование производительности

```bash
# Нагрузочное тестирование API
python -m pytest tests/performance/ -v

# Бенчмарки
python -m pytest tests/benchmarks/ -v
```

## 🔄 CI/CD

### GitHub Actions

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest tests/
      - run: behave features/
```

### Локальная проверка

```bash
# Полная проверка перед коммитом
./scripts/check-all.sh

# Проверка только изменённых файлов
./scripts/check-changed.sh
```

## 📝 Документация

### Генерация документации

```bash
# API документация
python -m src.mcp_server.main --docs

# Генерация README
python scripts/generate-readme.py

# Обновление планов
python scripts/update-plans.py
```

### Структура документации

```
docs/
├── DEVELOPMENT.md           # Это руководство
├── API.md                  # API документация
├── DEPLOYMENT.md           # Развертывание
├── CONTRIBUTING.md         # Вклад в проект
└── ARCHITECTURE.md         # Архитектурные решения
```

## 🚀 Развертывание

### Локальная разработка

```bash
# Запуск MCP сервера
uvicorn src.mcp_server.main:app --reload

# Запуск CLI
python -m src.cli.main index /path/to/testkit
python -m src.cli.main search "query"
```

### Docker

```bash
# Сборка образа
docker build -t testkitdex .

# Запуск контейнера
docker run -p 8000:8000 testkitdex

# Запуск с volumes
docker run -v /path/to/testkit:/data testkitdex index /data
```

## 🐛 Отладка

### Частые проблемы

1. **ImportError: No module named 'src'**
   ```bash
   export PYTHONPATH="${PYTHONPATH}:$(pwd)"
   ```

2. **SQLite database locked**
   ```bash
   # Проверьте, что нет других процессов
   lsof *.db
   ```

3. **MCP connection refused**
   ```bash
   # Проверьте, что сервер запущен
   curl http://localhost:8000/health
   ```

### Логирование

```python
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

## 🤝 Вклад в проект

### Создание Pull Request

1. **Fork репозитория**
2. **Создайте feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Следуйте TDD циклу**
   - BDD сценарий
   - Unit тесты
   - Реализация
   - Refactoring
4. **Проверьте качество**
   ```bash
   pre-commit run --all-files
   pytest tests/
   behave features/
   ```
5. **Создайте Pull Request**

### Code Review

- Все PR проходят review
- Требуется 2 approve для merge
- Обязательные проверки:
  - Тесты проходят
  - Покрытие не уменьшилось
  - Документация обновлена
  - Линтинг проходит

## 📚 Полезные ссылки

- [Планы разработки](plans/)
- [BDD сценарии](features/)
- [TestKit инфра](data/testkit_sample/)
- [API документация](docs/API.md)
- [Архитектура](docs/ARCHITECTURE.md)

---

**TestKitdex Development Guide** - Полное руководство по разработке 🚀 