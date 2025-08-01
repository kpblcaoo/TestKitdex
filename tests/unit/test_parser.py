"""
Unit tests for C# parser functionality.
"""
import pytest
from src.testkit_indexer.parser.csharp_parser import CSharpParser
from tests.factories import (
    create_user_factory_code,
    create_message_factory_code,
    create_generic_factory_code,
    create_simple_method_code,
    create_testkit_class_code
)


class TestCSharpParser:
    """Test C# parser functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.parser = CSharpParser()

    def test_extract_method_with_tags(self):
        """Test extracting methods with XML documentation tags."""
        # Given
        code = create_message_factory_code()
        
        # When
        methods = self.parser.extract_methods(code)
        
        # Then
        assert len(methods) == 1
        method = methods[0]
        assert method.name == "CreateMessage"
        assert method.tags == ["message", "factory", "telegram"]
        assert method.is_static is True
        assert method.return_type == "Message"

    def test_extract_method_without_tags(self):
        """Test extracting methods without tags."""
        # Given
        code = create_simple_method_code()
        
        # When
        methods = self.parser.extract_methods(code)
        
        # Then
        assert len(methods) == 1
        method = methods[0]
        assert method.name == "DoSomething"
        assert method.tags == []
        assert method.is_static is False
        assert method.return_type == "void"

    def test_extract_multiple_methods(self):
        """Test extracting multiple methods from a class."""
        # Given
        code = create_testkit_class_code()
        
        # When
        methods = self.parser.extract_methods(code)
        
        # Then
        assert len(methods) == 3
        
        create_user = methods[0]
        assert create_user.name == "CreateUser"
        assert create_user.tags == ["user", "factory", "test-data"]
        assert create_user.is_static is True
        
        create_message = methods[1]
        assert create_message.name == "CreateMessage"
        assert create_message.tags == ["message", "factory", "telegram"]
        assert create_message.is_static is True
        
        create_factory = methods[2]
        assert create_factory.name == "CreateFactory"
        assert create_factory.tags == ["factory", "generic"]
        assert create_factory.is_generic is True

    def test_handle_malformed_code(self):
        """Test handling malformed C# code gracefully."""
        # Given
        malformed_code = '''
        public class TestHelper {
            public static Message CreateMessage() {
                // Missing closing brace
        '''
        
        # When
        methods = self.parser.extract_methods(malformed_code)
        
        # Then
        # Should not raise exception, but may return empty list or partial results
        assert isinstance(methods, list)

    def test_extract_generic_methods(self):
        """Test extracting generic methods."""
        # Given
        code = create_generic_factory_code()
        
        # When
        methods = self.parser.extract_methods(code)
        
        # Then
        assert len(methods) == 1
        method = methods[0]
        assert method.name == "CreateFactory"
        assert method.tags == ["factory", "generic"]
        assert method.is_generic is True 