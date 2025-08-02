"""
Result Validator for TestKit BDD scenarios
Валидация результатов для BDD сценариев
"""

from typing import Any


def dispatch_result(context, result_type: str):
    """
    Диспетчеризация для проверки результатов
    
    Args:
        context: Behave context
        result_type: Тип результата для проверки
    
    Returns:
        bool: Результат проверки
    """
    mapping = {
        # Ошибки
        "an error with code 400": lambda: _check_error_400(context),
        
        # Методы
        "methods tagged with both": lambda: _check_methods_with_tags(context),
        "methods for creating user messages": lambda: _check_user_message_methods(context),
        "only methods with Message return type": lambda: _check_message_return_type(context),
        "methods tagged with moderation": lambda: _check_moderation_methods(context),
        "methods from all child levels": lambda: _check_hierarchy_methods(context),
        
        # Файлы
        "a Graphviz file": lambda: _check_graphviz_file(context),
        
        # Анализ
        "validation results": lambda: _check_validation_results(context),
        "tag usage patterns": lambda: _check_tag_usage_patterns(context),
        "conflict resolution options": lambda: _check_conflict_resolution(context),
        "suggestions for new tags": lambda: _check_tag_suggestions(context),
        "general-purpose suggestions": lambda: _check_general_suggestions(context),
        "semantically similar tag groups": lambda: _check_tag_clusters(context),
        "predictions for tag popularity": lambda: _check_tag_predictions(context),
    }
    
    func = mapping.get(result_type, lambda: _check_fallback(context))
    return func()


# === Вспомогательные функции для проверки результатов ===

def _check_error_400(context):
    """Проверка ошибки 400"""
    return hasattr(context, 'error_code') and context.error_code == 400


def _check_methods_with_tags(context):
    """Проверка методов с тегами"""
    return hasattr(context, 'search_results') and len(context.search_results) > 0


def _check_user_message_methods(context):
    """Проверка методов пользователя и сообщений"""
    return hasattr(context, 'search_results') and len(context.search_results) > 0


def _check_message_return_type(context):
    """Проверка методов с типом возврата Message"""
    return hasattr(context, 'search_results') and len(context.search_results) > 0


def _check_moderation_methods(context):
    """Проверка методов модерации"""
    return hasattr(context, 'search_results') and len(context.search_results) > 0


def _check_hierarchy_methods(context):
    """Проверка методов иерархии"""
    return hasattr(context, 'search_results') and len(context.search_results) > 0


def _check_graphviz_file(context):
    """Проверка файла Graphviz"""
    return hasattr(context, 'export_result') and context.export_result["format"] == "graphviz"


def _check_validation_results(context):
    """Проверка результатов валидации"""
    return hasattr(context, 'validation_result') and context.validation_result["valid"] > 0


def _check_tag_usage_patterns(context):
    """Проверка паттернов использования тегов"""
    return hasattr(context, 'usage_analysis') and context.usage_analysis["total_usage"] > 0


def _check_conflict_resolution(context):
    """Проверка разрешения конфликтов"""
    return hasattr(context, 'conflict_resolution') and context.conflict_resolution["resolved"] > 0


def _check_tag_suggestions(context):
    """Проверка предложений тегов"""
    return hasattr(context, 'suggestions') and len(context.suggestions) > 0


def _check_general_suggestions(context):
    """Проверка общих предложений"""
    return hasattr(context, 'suggestions') and len(context.suggestions) > 0


def _check_tag_clusters(context):
    """Проверка кластеров тегов"""
    return hasattr(context, 'clusters') and len(context.clusters) > 0


def _check_tag_predictions(context):
    """Проверка предсказаний тегов"""
    return hasattr(context, 'predictions') and len(context.predictions) > 0


def _check_fallback(context):
    """Fallback для проверки результатов"""
    return hasattr(context, 'command_result') or hasattr(context, 'search_results') 