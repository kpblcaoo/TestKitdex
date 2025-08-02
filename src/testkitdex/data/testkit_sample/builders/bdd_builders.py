"""
BDD Builders for TestKit scenarios
Универсальные билдеры для создания тестовых данных в BDD сценариях
"""

from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass
from src.testkit_indexer.parser.models import CSharpMethod
from data.testkit_sample.factories import CSharpMethodFactory, CSharpCodeFactory


@dataclass
class TestData:
    """Контейнер для тестовых данных"""
    methods: List[CSharpMethod] = None
    code_strings: List[str] = None
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.methods is None:
            self.methods = []
        if self.code_strings is None:
            self.code_strings = []
        if self.metadata is None:
            self.metadata = {}


class BDDDataBuilder:
    """Универсальный билдер для создания тестовых данных в BDD"""
    
    def __init__(self):
        self._test_data = TestData()
        self._method_builder = CSharpMethodBuilder()
        self._code_builder = CSharpCodeBuilder()
    
    # === Методы для создания данных ===
    
    def with_clean_database(self) -> 'BDDDataBuilder':
        """Создать чистую базу данных"""
        self._test_data.metadata['database_clean'] = True
        return self
    
    def with_indexed_methods(self, count: int = 10) -> 'BDDDataBuilder':
        """Создать индексированные методы"""
        for i in range(count):
            method = CSharpMethodFactory.create(
                name=f"Method{i}",
                return_type="User" if i % 2 == 0 else "Message",
                tags=["indexed", f"method{i}"],
                is_static=True
            )
            self._test_data.methods.append(method)
        return self
    
    def with_search_index(self) -> 'BDDDataBuilder':
        """Создать поисковый индекс"""
        self._test_data.metadata['search_index_built'] = True
        return self
    
    def with_test_data(self, **kwargs) -> 'BDDDataBuilder':
        """Создать тестовые данные с различными тегами"""
        # Создаем разнообразные методы
        test_methods = [
            ("CreateUser", "User", ["user", "factory", "test-data"]),
            ("CreateMessage", "Message", ["message", "factory", "telegram"]),
            ("CreateFactory", "T", ["factory", "generic"]),
            ("ValidateUser", "bool", ["validation", "user"]),
            ("ProcessData", "string", ["processing", "data"]),
        ]
        
        for name, return_type, tags in test_methods:
            method = CSharpMethodFactory.create(
                name=name,
                return_type=return_type,
                tags=tags,
                is_static=True
            )
            self._test_data.methods.append(method)
        
        return self
    
    def with_conflicting_tags(self) -> 'BDDDataBuilder':
        """Создать конфликтующие теги"""
        conflicting_methods = [
            ("CreateUser", "User", ["user", "factory"]),
            ("CreateUser", "User", ["user", "helper"]),  # Конфликт
            ("ValidateUser", "bool", ["user", "validation"]),
            ("ValidateUser", "bool", ["user", "check"]),  # Конфликт
        ]
        
        for name, return_type, tags in conflicting_methods:
            method = CSharpMethodFactory.create(
                name=name,
                return_type=return_type,
                tags=tags,
                is_static=True
            )
            self._test_data.methods.append(method)
        
        return self
    
    def with_large_dataset(self, method_count: int = 10000) -> 'BDDDataBuilder':
        """Создать большой набор данных"""
        for i in range(method_count):
            method = CSharpMethodFactory.create(
                name=f"LargeMethod{i}",
                return_type="User" if i % 3 == 0 else "Message" if i % 3 == 1 else "bool",
                tags=["large", "dataset", f"type{i % 10}"],
                is_static=i % 2 == 0
            )
            self._test_data.methods.append(method)
        
        self._test_data.metadata['large_dataset'] = True
        return self
    
    def with_malformed_files(self) -> 'BDDDataBuilder':
        """Создать файлы с ошибками"""
        malformed_code = '''
        public class TestHelper {
            public static Message CreateMessage() {
                // Missing closing brace
        '''
        self._test_data.code_strings.append(malformed_code)
        self._test_data.metadata['malformed_files'] = True
        return self
    
    def with_xml_documentation(self) -> 'BDDDataBuilder':
        """Создать методы с XML документацией"""
        documented_method = CSharpMethodFactory.create(
            name="CreateDocumentedUser",
            return_type="User",
            parameters=["string name", "string email"],
            tags=["user", "factory", "documented"],
            summary="Creates a test user with comprehensive documentation",
            is_static=True
        )
        self._test_data.methods.append(documented_method)
        return self
    
    def with_complex_signatures(self) -> 'BDDDataBuilder':
        """Создать методы со сложными сигнатурами"""
        complex_method = CSharpMethodFactory.create(
            name="FilterItems",
            return_type="List<T>",
            parameters=["IEnumerable<T> items", "Func<T, bool> predicate"],
            tags=["generic", "filter", "factory"],
            is_generic=True,
            is_static=True
        )
        self._test_data.methods.append(complex_method)
        return self
    
    def with_tag_hierarchy(self) -> 'BDDDataBuilder':
        """Создать иерархию тегов"""
        hierarchy_methods = [
            ("BanUser", "bool", ["moderation", "ban"]),
            ("WarnUser", "bool", ["moderation", "warn"]),
            ("CreateUser", "User", ["user", "factory"]),
            ("CreateMessage", "Message", ["message", "factory"]),
        ]
        
        for name, return_type, tags in hierarchy_methods:
            method = CSharpMethodFactory.create(
                name=name,
                return_type=return_type,
                tags=tags,
                is_static=True
            )
            self._test_data.methods.append(method)
        
        self._test_data.metadata['tag_hierarchy'] = True
        return self
    
    def with_ai_capabilities(self) -> 'BDDDataBuilder':
        """Создать данные для AI анализа"""
        ai_methods = [
            ("SuggestTags", "List<string>", ["ai", "suggestions"]),
            ("AnalyzeTags", "AnalysisResult", ["ai", "analysis"]),
            ("PredictUsage", "Prediction", ["ai", "prediction"]),
        ]
        
        for name, return_type, tags in ai_methods:
            method = CSharpMethodFactory.create(
                name=name,
                return_type=return_type,
                tags=tags,
                is_static=True
            )
            self._test_data.methods.append(method)
        
        self._test_data.metadata['ai_capabilities'] = True
        return self
    
    # === Методы для создания контекста ===
    
    def with_context(self, context_type: str, **kwargs) -> 'BDDDataBuilder':
        """Создать контекст для тестирования"""
        self._test_data.metadata['context'] = {
            'type': context_type,
            'data': kwargs
        }
        return self
    
    def with_task_description(self, description: str) -> 'BDDDataBuilder':
        """Создать описание задачи"""
        self._test_data.metadata['task_description'] = description
        return self
    
    # === Методы для создания сценариев ===
    
    def for_search_scenario(self) -> 'BDDDataBuilder':
        """Настроить для сценария поиска"""
        return (self
            .with_clean_database()
            .with_indexed_methods(100)
            .with_search_index()
            .with_test_data())
    
    def for_tag_analysis_scenario(self) -> 'BDDDataBuilder':
        """Настроить для сценария анализа тегов"""
        return (self
            .with_clean_database()
            .with_indexed_methods(50)
            .with_tag_hierarchy()
            .with_ai_capabilities())
    
    def for_indexing_scenario(self) -> 'BDDDataBuilder':
        """Настроить для сценария индексации"""
        return (self
            .with_clean_database()
            .with_test_data()
            .with_xml_documentation()
            .with_complex_signatures())
    
    def for_performance_scenario(self) -> 'BDDDataBuilder':
        """Настроить для сценария производительности"""
        return (self
            .with_clean_database()
            .with_large_dataset(1000)
            .with_search_index())
    
    def for_error_scenario(self) -> 'BDDDataBuilder':
        """Настроить для сценария обработки ошибок"""
        return (self
            .with_clean_database()
            .with_malformed_files()
            .with_conflicting_tags())
    
    # === Методы для получения данных ===
    
    def build(self) -> TestData:
        """Создать тестовые данные"""
        return self._test_data
    
    def get_methods(self) -> List[CSharpMethod]:
        """Получить список методов"""
        return self._test_data.methods
    
    def get_code_strings(self) -> List[str]:
        """Получить список строк кода"""
        return self._test_data.code_strings
    
    def get_metadata(self) -> Dict[str, Any]:
        """Получить метаданные"""
        return self._test_data.metadata


class CSharpMethodBuilder:
    """Билдер для C# методов с Fluent API"""
    
    def __init__(self):
        self._method_data = {}
        self._use_factory = False
        self._factory_method = None
    
    def with_name(self, name: str) -> 'CSharpMethodBuilder':
        self._method_data['name'] = name
        return self
    
    def with_return_type(self, return_type: str) -> 'CSharpMethodBuilder':
        self._method_data['return_type'] = return_type
        return self
    
    def with_tags(self, *tags: str) -> 'CSharpMethodBuilder':
        self._method_data['tags'] = list(tags)
        return self
    
    def with_parameters(self, *parameters: str) -> 'CSharpMethodBuilder':
        self._method_data['parameters'] = list(parameters)
        return self
    
    def with_summary(self, summary: str) -> 'CSharpMethodBuilder':
        self._method_data['summary'] = summary
        return self
    
    def static(self) -> 'CSharpMethodBuilder':
        self._method_data['is_static'] = True
        return self
    
    def generic(self) -> 'CSharpMethodBuilder':
        self._method_data['is_generic'] = True
        return self
    
    def public(self) -> 'CSharpMethodBuilder':
        self._method_data['is_public'] = True
        return self
    
    def private(self) -> 'CSharpMethodBuilder':
        self._method_data['is_public'] = False
        return self
    
    # Фабричные методы
    def as_user_factory(self) -> 'CSharpMethodBuilder':
        self._use_factory = True
        self._factory_method = 'create_user_factory_method'
        return self
    
    def as_message_factory(self) -> 'CSharpMethodBuilder':
        self._use_factory = True
        self._factory_method = 'create_message_factory_method'
        return self
    
    def as_generic_factory(self) -> 'CSharpMethodBuilder':
        self._use_factory = True
        self._factory_method = 'create_generic_factory_method'
        return self
    
    def build(self) -> CSharpMethod:
        if self._use_factory:
            factory_method = getattr(CSharpMethodFactory, self._factory_method)
            return factory_method()
        else:
            return CSharpMethod(**self._method_data)


class CSharpCodeBuilder:
    """Билдер для C# кода с Fluent API"""
    
    def __init__(self):
        self._code_data = {}
        self._use_factory = False
        self._factory_method = None
    
    def with_method_name(self, name: str) -> 'CSharpCodeBuilder':
        self._code_data['method_name'] = name
        return self
    
    def with_return_type(self, return_type: str) -> 'CSharpCodeBuilder':
        self._code_data['return_type'] = return_type
        return self
    
    def with_tags(self, *tags: str) -> 'CSharpCodeBuilder':
        self._code_data['tags'] = list(tags)
        return self
    
    def with_parameters(self, *parameters: str) -> 'CSharpCodeBuilder':
        self._code_data['parameters'] = list(parameters)
        return self
    
    def with_summary(self, summary: str) -> 'CSharpCodeBuilder':
        self._code_data['summary'] = summary
        return self
    
    def static(self) -> 'CSharpCodeBuilder':
        self._code_data['is_static'] = True
        return self
    
    def generic(self) -> 'CSharpCodeBuilder':
        self._code_data['is_generic'] = True
        return self
    
    # Фабричные методы
    def as_user_factory_code(self) -> 'CSharpCodeBuilder':
        self._use_factory = True
        self._factory_method = 'create_user_factory_code'
        return self
    
    def as_message_factory_code(self) -> 'CSharpCodeBuilder':
        self._use_factory = True
        self._factory_method = 'create_message_factory_code'
        return self
    
    def as_generic_factory_code(self) -> 'CSharpCodeBuilder':
        self._use_factory = True
        self._factory_method = 'create_generic_factory_code'
        return self
    
    def build(self) -> str:
        if self._use_factory:
            factory_method = getattr(CSharpCodeFactory, self._factory_method)
            return factory_method()
        else:
            # Создать код на основе данных
            return self._generate_code()
    
    def _generate_code(self) -> str:
        """Генерировать код на основе данных"""
        method_name = self._code_data.get('method_name', 'TestMethod')
        return_type = self._code_data.get('return_type', 'void')
        parameters = self._code_data.get('parameters', [])
        tags = self._code_data.get('tags', [])
        summary = self._code_data.get('summary', '')
        is_static = self._code_data.get('is_static', False)
        
        static_keyword = "static " if is_static else ""
        params_str = ", ".join(parameters) if parameters else ""
        tags_str = ", ".join(tags) if tags else ""
        
        code = f'''
        /// <summary>
        /// {summary}
        /// </summary>
        /// <tags>{tags_str}</tags>
        public {static_keyword}{return_type} {method_name}({params_str})
        {{
            // Implementation
            return default({return_type});
        }}
        '''
        return code


# Глобальные функции для удобства
def create_bdd_data() -> BDDDataBuilder:
    """Создать билдер для BDD данных"""
    return BDDDataBuilder()

def create_method_builder() -> CSharpMethodBuilder:
    """Создать билдер для C# методов"""
    return CSharpMethodBuilder()

def create_code_builder() -> CSharpCodeBuilder:
    """Создать билдер для C# кода"""
    return CSharpCodeBuilder() 