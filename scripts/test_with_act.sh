#!/bin/bash

# TestKitdex Act Integration Script
# Локальное тестирование GitHub Actions

set -e

echo "🧪 TestKitdex Act Integration"
echo "=============================="

# Проверяем наличие Act
if ! command -v act &> /dev/null; then
    echo "❌ Act не установлен. Установите: https://nektosact.com/"
    exit 1
fi

echo "✅ Act найден: $(act --version)"

# Создаем временную директорию для артефактов
ARTIFACT_DIR="/tmp/testkitdex-artifacts"
mkdir -p "$ARTIFACT_DIR"
echo "📁 Артефакты: $ARTIFACT_DIR"

# Функция для тестирования workflow
test_workflow() {
    local event=$1
    local workflow=$2
    
    echo ""
    echo "🔄 Тестируем $workflow ($event)..."
    
    if act "$event" --workflows "$workflow" --dry-run; then
        echo "✅ $workflow ($event) - OK"
    else
        echo "❌ $workflow ($event) - FAILED"
        return 1
    fi
}

# Функция для тестирования с реальными данными
test_with_data() {
    local event=$1
    
    echo ""
    echo "🎯 Тестируем $event с реальными данными..."
    
    if act "$event" --artifact-server-path "$ARTIFACT_DIR" --verbose; then
        echo "✅ $event с данными - OK"
    else
        echo "❌ $event с данными - FAILED"
        return 1
    fi
}

# Основные тесты
echo ""
echo "📋 Запуск тестов..."

# Тестируем push workflow
test_workflow "push" ".github/workflows/test.yml"

# Тестируем pull_request workflow
test_workflow "pull_request" ".github/workflows/test.yml"

# Тестируем с реальными данными (опционально)
if [[ "$1" == "--with-data" ]]; then
    test_with_data "push"
    test_with_data "pull_request"
fi

echo ""
echo "🎉 Все тесты завершены!"
echo "📁 Артефакты сохранены в: $ARTIFACT_DIR"

# Очистка
echo ""
echo "🧹 Очистка временных файлов..."
rm -rf "$ARTIFACT_DIR"

echo "✅ Готово!" 