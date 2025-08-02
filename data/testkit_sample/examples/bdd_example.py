"""
Пример использования BDD билдеров для TestKit
Демонстрирует возможности универсальных билдеров для BDD сценариев
"""

from data.testkit_sample.builders import (
    create_bdd_data,
    create_method_builder,
    create_code_builder
)


def demonstrate_bdd_builders():
    """Демонстрация возможностей BDD билдеров"""
    
    print("=== BDD Data Builder Examples ===\n")
    
    # 1. Создание данных для сценария поиска
    print("1. Создание данных для сценария поиска:")
    search_data = (create_bdd_data()
        .for_search_scenario()
        .build())
    
    print(f"   - Методов: {len(search_data.methods)}")
    print(f"   - Метаданные: {search_data.metadata}")
    print()
    
    # 2. Создание данных для сценария анализа тегов
    print("2. Создание данных для сценария анализа тегов:")
    tag_analysis_data = (create_bdd_data()
        .for_tag_analysis_scenario()
        .build())
    
    print(f"   - Методов: {len(tag_analysis_data.methods)}")
    print(f"   - AI возможности: {tag_analysis_data.metadata.get('ai_capabilities', False)}")
    print()
    
    # 3. Создание данных для сценария производительности
    print("3. Создание данных для сценария производительности:")
    performance_data = (create_bdd_data()
        .for_performance_scenario()
        .build())
    
    print(f"   - Методов: {len(performance_data.methods)}")
    print(f"   - Большой набор данных: {performance_data.metadata.get('large_dataset', False)}")
    print()
    
    # 4. Создание данных для сценария обработки ошибок
    print("4. Создание данных для сценария обработки ошибок:")
    error_data = (create_bdd_data()
        .for_error_scenario()
        .build())
    
    print(f"   - Методов: {len(error_data.methods)}")
    print(f"   - Файлы с ошибками: {error_data.metadata.get('malformed_files', False)}")
    print()
    
    print("=== Method Builder Examples ===\n")
    
    # 5. Создание метода через билдер
    print("5. Создание метода через билдер:")
    method = (create_method_builder()
        .with_name("CustomMethod")
        .with_return_type("string")
        .with_tags("custom", "test")
        .with_parameters("int id", "string name")
        .static()
        .build())
    
    print(f"   - Имя: {method.name}")
    print(f"   - Возвращаемый тип: {method.return_type}")
    print(f"   - Теги: {method.tags}")
    print(f"   - Статический: {method.is_static}")
    print()
    
    # 6. Создание метода через фабрику через билдер
    print("6. Создание метода через фабрику через билдер:")
    factory_method = (create_method_builder()
        .as_user_factory()
        .build())
    
    print(f"   - Имя: {factory_method.name}")
    print(f"   - Возвращаемый тип: {factory_method.return_type}")
    print(f"   - Теги: {factory_method.tags}")
    print()
    
    print("=== Code Builder Examples ===\n")
    
    # 7. Создание кода через билдер
    print("7. Создание кода через билдер:")
    code = (create_code_builder()
        .with_method_name("TestMethod")
        .with_return_type("void")
        .with_tags("test", "example")
        .with_summary("Test method for demonstration")
        .static()
        .build())
    
    print("   Сгенерированный код:")
    print(code)
    print()
    
    # 8. Создание кода через фабрику через билдер
    print("8. Создание кода через фабрику через билдер:")
    factory_code = (create_code_builder()
        .as_user_factory_code()
        .build())
    
    print("   Код фабрики пользователя:")
    print(factory_code)
    print()
    
    print("=== Advanced Examples ===\n")
    
    # 9. Создание сложного сценария
    print("9. Создание сложного сценария:")
    complex_data = (create_bdd_data()
        .with_clean_database()
        .with_indexed_methods(100)
        .with_search_index()
        .with_test_data()
        .with_tag_hierarchy()
        .with_ai_capabilities()
        .with_xml_documentation()
        .with_complex_signatures()
        .with_context("complex_scenario", complexity="high")
        .with_task_description("Create comprehensive test scenario")
        .build())
    
    print(f"   - Методов: {len(complex_data.methods)}")
    print(f"   - Строк кода: {len(complex_data.code_strings)}")
    print(f"   - Метаданные: {len(complex_data.metadata)}")
    print(f"   - Контекст: {complex_data.metadata.get('context', {}).get('type', 'none')}")
    print()
    
    # 10. Создание множества методов с разными параметрами
    print("10. Создание множества методов с разными параметрами:")
    methods = []
    
    for i in range(5):
        builder = create_method_builder()
        builder = builder.with_name(f"Method{i}")
        builder = builder.with_return_type("User" if i % 2 == 0 else "Message")
        builder = builder.with_tags(f"type{i}", "test")
        builder = builder.with_parameters(f"int param{i}")
        if i % 2 == 0:
            builder = builder.static()
        method = builder.build()
        methods.append(method)
    
    print(f"   - Создано методов: {len(methods)}")
    for method in methods:
        print(f"     * {method.name}: {method.return_type} (теги: {method.tags})")
    print()
    
    print("=== Summary ===")
    print("BDD билдеры предоставляют:")
    print("- Универсальный API для создания тестовых данных")
    print("- Интеграцию с существующими фабриками")
    print("- Поддержку Fluent API для читаемости")
    print("- Параметризованные шаги для BDD сценариев")
    print("- Готовые сценарии для разных типов тестов")


if __name__ == "__main__":
    demonstrate_bdd_builders() 