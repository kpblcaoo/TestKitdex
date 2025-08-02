"""
Factory for creating C# code in tests.
"""
from typing import List, Optional


class CSharpCodeFactory:
    """Factory for creating C# code in tests."""
    
    @staticmethod
    def create_method_with_tags(
        method_name: str = "CreateMessage",
        return_type: str = "Message",
        parameters: Optional[List[str]] = None,
        tags: Optional[List[str]] = None,
        summary: str = "Creates a test message",
        is_static: bool = True,
        is_public: bool = True
    ) -> str:
        """Create a C# method with XML documentation and tags."""
        if parameters is None:
            parameters = []
        if tags is None:
            tags = ["message", "factory", "telegram"]
            
        # Build method signature
        access_modifier = "public " if is_public else ""
        static_modifier = "static " if is_static else ""
        params_str = ", ".join(parameters) if parameters else ""
        
        # Build tags string
        tags_str = ", ".join(tags)
        
        # Create XML documentation
        xml_doc = f'''        /// <summary>
        /// {summary}
        /// <tags>{tags_str}</tags>
        /// </summary>'''
        
        # Create method
        method = f'''{xml_doc}
        {access_modifier}{static_modifier}{return_type} {method_name}({params_str}) {{
            // implementation
        }}'''
        
        return method
    
    @staticmethod
    def create_simple_method(
        method_name: str = "DoSomething",
        return_type: str = "void",
        parameters: Optional[List[str]] = None,
        is_public: bool = True
    ) -> str:
        """Create a simple C# method without XML documentation."""
        if parameters is None:
            parameters = []
            
        access_modifier = "public " if is_public else ""
        params_str = ", ".join(parameters) if parameters else ""
        
        method = f'''        {access_modifier}{return_type} {method_name}({params_str}) {{
            // implementation
        }}'''
        
        return method
    
    @staticmethod
    def create_generic_method(
        method_name: str = "CreateFactory",
        return_type: str = "T",
        parameters: Optional[List[str]] = None,
        tags: Optional[List[str]] = None,
        summary: str = "Generic factory method"
    ) -> str:
        """Create a generic C# method."""
        if parameters is None:
            parameters = []
        if tags is None:
            tags = ["factory", "generic"]
            
        tags_str = ", ".join(tags)
        params_str = ", ".join(parameters) if parameters else ""
        
        xml_doc = f'''        /// <summary>
        /// {summary}
        /// <tags>{tags_str}</tags>
        /// </summary>'''
        
        method = f'''{xml_doc}
        public static {return_type} {method_name}<T>({params_str}) where T : class, new() {{
            return new T();
        }}'''
        
        return method
    
    @staticmethod
    def create_class_with_methods(
        class_name: str = "TestDataFactory",
        methods: Optional[List[str]] = None,
        is_static: bool = True
    ) -> str:
        """Create a C# class with multiple methods."""
        if methods is None:
            methods = [
                CSharpCodeFactory.create_method_with_tags(
                    "CreateUser", "User", ["string name = \"TestUser\""],
                    ["user", "factory", "test-data"], "Creates a test user"
                ),
                CSharpCodeFactory.create_method_with_tags(
                    "CreateMessage", "Message", ["string text = \"Test message\""],
                    ["message", "factory", "telegram"], "Creates a test message"
                ),
                CSharpCodeFactory.create_generic_method(
                    "CreateFactory", "T", [], ["factory", "generic"], "Generic factory method"
                )
            ]
        
        static_modifier = "static " if is_static else ""
        methods_str = "\n\n".join(methods)
        
        class_code = f'''using System;

namespace TestKit.Sample
{{
    /// <summary>
    /// Helper class for creating test data
    /// <tags>factory, test-data, helper</tags>
    /// </summary>
    public {static_modifier}class {class_name}
    {{
{methods_str}
    }}
}}'''
        
        return class_code
    
    @staticmethod
    def create_malformed_code() -> str:
        """Create malformed C# code for testing error handling."""
        return '''public class TestHelper {
    public static Message CreateMessage() {
        // Missing closing brace
'''
    
    @staticmethod
    def create_method_with_complex_signature() -> str:
        """Create a method with complex signature."""
        return '''        /// <summary>
        /// Creates a complex object
        /// <tags>complex, factory, builder</tags>
        /// </summary>
        public static ComplexObject CreateComplexObject<T>(
            string name, 
            int count = 0, 
            params object[] args) where T : class
        {
            return new ComplexObject();
        }'''


# Convenience functions
def create_user_factory_code() -> str:
    """Create user factory method code."""
    return CSharpCodeFactory.create_method_with_tags(
        "CreateUser", "User", ["string name = \"TestUser\""],
        ["user", "factory", "test-data"], "Creates a test user"
    )


def create_message_factory_code() -> str:
    """Create message factory method code."""
    return CSharpCodeFactory.create_method_with_tags(
        "CreateMessage", "Message", ["string text = \"Test message\""],
        ["message", "factory", "telegram"], "Creates a test message"
    )


def create_generic_factory_code() -> str:
    """Create generic factory method code."""
    return CSharpCodeFactory.create_generic_method()


def create_simple_method_code() -> str:
    """Create simple method code."""
    return CSharpCodeFactory.create_simple_method()


def create_testkit_class_code() -> str:
    """Create TestKit class with multiple methods."""
    return CSharpCodeFactory.create_class_with_methods() 