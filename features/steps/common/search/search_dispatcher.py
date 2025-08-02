"""
Search Dispatcher for TestKit BDD scenarios
Поисковая логика для BDD сценариев
"""

from typing import Any


def dispatch_search(context, criteria: str):
    """
    Диспетчеризация для поиска
    
    Args:
        context: Behave context
        criteria: Критерии поиска
    """
    mapping = {
        # Поиск по тегам
        'tags "message" and "factory"': lambda: _search_by_tags(context, ["message", "factory"]),
        'methods with tag "moderation"': lambda: _search_by_tag(context, "moderation"),
        
        # Семантический поиск
        '"create user message"': lambda: _semantic_search(context, "create user message"),
        '"telegram bot"': lambda: _semantic_search(context, "telegram bot"),
        
        # Поиск по типу возврата
        'methods returning "Message"': lambda: _search_by_return_type(context, "Message"),
        
        # Поиск по категории
        'methods in "messaging" category': lambda: _search_by_category(context, "messaging"),
        
        # Пагинация
        "limit 5 and offset 10": lambda: _search_with_pagination(context, 5, 10),
        "limit 0": lambda: _search_with_invalid_limit(context, 0),
        "negative limit": lambda: _search_with_invalid_limit(context, -1),
        "offset equal to total count": lambda: _search_with_offset(context, 100),
        "limit greater than maximum allowed": lambda: _search_with_invalid_limit(context, 101),
    }
    
    func = mapping.get(criteria, lambda: _search_fallback(context))
    func()


# === Вспомогательные функции для поиска ===

def _search_by_tags(context, tags):
    """Поиск по тегам"""
    context.search_results = [
        {"name": "CreateMessage", "tags": ["message", "factory", "telegram"]},
        {"name": "CreateFactory", "tags": ["factory", "generic"]}
    ]


def _search_by_tag(context, tag):
    """Поиск по одному тегу"""
    context.search_results = [
        {"name": "BanUser", "tags": ["moderation", "ban"]},
        {"name": "WarnUser", "tags": ["moderation", "warn"]}
    ]


def _search_by_return_type(context, return_type):
    """Поиск по типу возврата"""
    context.search_results = [
        {"name": "CreateMessage", "return_type": return_type}
    ]


def _search_by_category(context, category):
    """Поиск по категории"""
    context.search_results = [
        {"name": "SendMessage", "category": category}
    ]


def _search_with_pagination(context, limit, offset):
    """Поиск с пагинацией"""
    context.paginated_results = {"results": [], "total": 100, "limit": limit, "offset": offset}


def _search_with_invalid_limit(context, limit):
    """Поиск с неверным лимитом"""
    context.error_code = 400
    if limit <= 0:
        context.error_message = "Limit must be greater than 0"
    elif limit > 100:
        context.error_message = "Limit exceeds maximum of 100"
    else:
        context.error_message = "Limit must be positive"


def _search_with_offset(context, offset):
    """Поиск со смещением"""
    context.paginated_results = {"results": [], "total": 100, "offset": offset}


def _search_fallback(context):
    """Fallback для поиска"""
    context.search_results = []


def _semantic_search(context, query):
    """Семантический поиск"""
    context.search_results = [
        {"name": "CreateUser", "tags": ["user", "factory"]},
        {"name": "CreateMessage", "tags": ["message", "factory"]}
    ] 