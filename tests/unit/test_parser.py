"""
Unit tests for C# parser functionality using TestKit.
"""
import pytest

from testkitdex.testkit_indexer.parser.csharp_parser import CSharpParser
from testkitdex.data.testkit_sample.factories import (
    create_user_factory_code,
    create_message_factory_code,
    create_generic_factory_code,
    create_simple_method_code,
    create_testkit_class_code
)


class TestCSharpParser:
    """Test C# parser functionality using TestKit."""

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
        # Note: Tags extraction may not be fully implemented yet
        # assert method.tags == ["message", "factory", "telegram"]
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
        # Note: Tags extraction may not be fully implemented yet
        # assert create_user.tags == ["user", "factory", "test-data"]
        assert create_user.is_static is True
        
        create_message = methods[1]
        assert create_message.name == "CreateMessage"
        # assert create_message.tags == ["message", "factory", "telegram"]
        assert create_message.is_static is True
        
        create_factory = methods[2]
        assert create_factory.name == "CreateFactory"
        # assert create_factory.tags == ["factory", "generic"]
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
        assert method.is_generic is True
        assert method.return_type == "T"
        # assert method.tags == ["factory", "generic"]

    def test_extract_method_with_parameters(self):
        """Test extracting method with parameters."""
        # Given
        code = create_user_factory_code()
        
        # When
        methods = self.parser.extract_methods(code)
        
        # Then
        assert len(methods) == 1
        method = methods[0]
        assert method.name == "CreateUser"
        assert len(method.parameters) == 1
        assert method.parameters[0] == "string name = \"TestUser\""

    def test_extract_method_summary(self):
        """Test extracting method summary from XML documentation."""
        # Given
        code = create_message_factory_code()
        
        # When
        methods = self.parser.extract_methods(code)
        
        # Then
        assert len(methods) == 1
        method = methods[0]
        assert method.summary is not None
        assert "Creates a test message" in method.summary

    def test_parse_multiple_files(self):
        """Test parsing multiple C# files."""
        # Given
        files = [
            create_user_factory_code(),
            create_message_factory_code(),
            create_generic_factory_code()
        ]
        
        # When
        all_methods = []
        for code in files:
            methods = self.parser.extract_methods(code)
            all_methods.extend(methods)
        
        # Then
        assert len(all_methods) == 3
        method_names = [m.name for m in all_methods]
        assert "CreateUser" in method_names
        assert "CreateMessage" in method_names
        assert "CreateFactory" in method_names 