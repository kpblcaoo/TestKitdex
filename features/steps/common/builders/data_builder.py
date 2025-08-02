"""
Data Builder for TestKit BDD scenarios
Создание тестовых данных для BDD сценариев
"""

from typing import Any


def dispatch(builder, spec: str):
    """
    Диспетчеризация для создания данных
    
    Args:
        builder: BDD builder instance
        spec: Спецификация данных (например, "a clean database")
    
    Returns:
        Builder с примененной конфигурацией
    """
    mapping = {
        # Базовые данные
        "a clean database": builder.with_clean_database,
        "indexed TestKit methods": lambda: builder.with_indexed_methods(50),
        "test data with various tags and methods": builder.with_test_data,
        "the search index is built": builder.with_search_index,
        "the AI analysis engine is trained": builder.with_ai_capabilities,
        
        # Большие наборы данных
        "10000 indexed methods": lambda: builder.with_large_dataset(10000),
        "TestKit with 10000+ methods": lambda: builder.with_large_dataset(10000),
        "1000+ tags to analyze": lambda: builder.with_large_dataset(1000),
        "100000+ usage records": lambda: builder.with_large_dataset(100000),
        
        # Специальные данные
        "conflicting tag definitions": builder.with_conflicting_tags,
        "malformed C# files": builder.with_malformed_files,
        "methods with XML documentation": builder.with_xml_documentation,
        "methods with multiple tags": builder.with_test_data,
        "static and instance methods": builder.with_test_data,
        "generic and non-generic methods": builder.with_complex_signatures,
        "a C# method with complex signature": builder.with_complex_signatures,
        
        # Иерархии и контексты
        "a tag hierarchy with moderation as parent": builder.with_tag_hierarchy,
        "a tag hierarchy in JSON format": builder.with_tag_hierarchy,
        "two different tag hierarchies": builder.with_tag_hierarchy,
        "a deep tag hierarchy": builder.with_tag_hierarchy,
        "a complex context": lambda: builder.with_context("complex"),
        "a task description": lambda: builder.with_task_description("create telegram bot test"),
        "an existing indexed TestKit": builder.with_test_data,
        "new or modified files": builder.with_test_data,
        "C# files with tagged methods": builder.with_test_data,
        
        # Специальные контексты
        "context I need to create a test user with a message": lambda: builder.with_context("user_message"),
        "context about user management": lambda: builder.with_context("user_management"),
        "indexed TestKit with usage data": builder.with_test_data,
        "indexed TestKit with AI capabilities": builder.with_ai_capabilities,
        "methods that are never used": builder.with_test_data,
        
        # Данные с условиями (для шагов "with {condition}")
        "context with user_message": lambda: builder.with_context("user_message"),
        "context with user_management": lambda: builder.with_context("user_management"),
        "context with complex": lambda: builder.with_context("complex"),
        "a task description with create telegram bot test": lambda: builder.with_task_description("create telegram bot test"),
        "a task description with create user test": lambda: builder.with_task_description("create user test"),
        "a tag hierarchy with moderation as parent with moderation": lambda: builder.with_tag_hierarchy(),
        "a tag hierarchy in JSON format with json": lambda: builder.with_tag_hierarchy(),
        "two different tag hierarchies with merge": lambda: builder.with_tag_hierarchy(),
        "a deep tag hierarchy with nested": lambda: builder.with_tag_hierarchy(),
        "a C# method with complex signature with generic": lambda: builder.with_complex_signatures(),
        "1000+ tags to analyze with clustering": lambda: builder.with_large_dataset(1000),
        "100000+ usage records with patterns": lambda: builder.with_large_dataset(100000),
        "static and instance methods with both": lambda: builder.with_test_data(),
        "methods with XML documentation with docs": lambda: builder.with_xml_documentation(),
        "generic and non-generic methods with mixed": lambda: builder.with_complex_signatures(),
        "an existing indexed TestKit with data": lambda: builder.with_test_data(),
        "new or modified files with changes": lambda: builder.with_test_data(),
        "C# files with tagged methods with tags": lambda: builder.with_test_data(),
    }
    
    # Получаем функцию из маппинга или используем fallback
    func = mapping.get(spec, builder.with_test_data)
    
    # Вызываем функцию (с поддержкой как методов, так и лямбда-функций)
    if callable(func):
        return func()
    else:
        return builder.with_test_data() 