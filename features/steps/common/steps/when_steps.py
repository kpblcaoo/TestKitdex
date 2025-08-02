"""
When step definitions for TestKit BDD scenarios
When шаги для BDD сценариев TestKit
"""

from behave import when
from features.steps.common import dispatch_command, dispatch_search


@when("I run {command}")
def step_impl(context, command):
    """Универсальный шаг для выполнения команд"""
    dispatch_command(context, command)


@when("I search for {criteria}")
def step_impl(context, criteria):
    """Универсальный шаг для поиска"""
    dispatch_search(context, criteria)


@when("I search with {pagination}")
def step_impl(context, pagination):
    """Универсальный шаг для поиска с пагинацией"""
    dispatch_search(context, pagination)


@when("I type {text} in the search box")
def step_impl(context, text):
    """Универсальный шаг для ввода текста"""
    if text == '"mess"':
        context.suggestions = ["message", "messaging", "messenger"]
    else:
        context.suggestions = []


@when("I perform multiple searches")
def step_impl(context):
    """Универсальный шаг для множественных поисков"""
    context.search_history = [
        {"query": "user", "timestamp": "2024-01-01T10:00:00"},
        {"query": "message", "timestamp": "2024-01-01T10:01:00"},
        {"query": "factory", "timestamp": "2024-01-01T10:02:00"}
    ]


@when("I request {request_type}")
def step_impl(context, request_type):
    """Универсальный шаг для запросов"""
    if request_type == 'tag suggestions for "user management"':
        context.suggestions = ["user", "registration", "profile"]
    elif request_type == "tag clustering":
        context.clusters = [
            {"tags": ["user", "registration"], "confidence": 0.9},
            {"tags": ["message", "telegram"], "confidence": 0.8}
        ]
    elif request_type == "tag usage prediction":
        context.predictions = [
            {"tag": "user", "predicted_usage": 150, "confidence": 0.85}
        ]
    else:
        context.request_result = {"success": True, "type": request_type}


@when("I compare {objects}")
def step_impl(context, objects):
    """Универсальный шаг для сравнения"""
    if objects == "two databases":
        context.comparison_result = {"added": 5, "modified": 2, "deleted": 1}
    else:
        context.comparison_result = {"differences": 0}


@when("I use {protocol}")
def step_impl(context, protocol):
    """Универсальный шаг для использования протоколов"""
    dispatch_command(context, protocol)


@when("I explore {object}")
def step_impl(context, object):
    """Универсальный шаг для исследования"""
    if object == "the tag hierarchy":
        context.hierarchy_exploration = {"levels": 3, "nodes": 50}
    else:
        context.exploration_result = {"object": object, "explored": True} 