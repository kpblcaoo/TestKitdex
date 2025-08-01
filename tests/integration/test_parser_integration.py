"""
Integration tests for C# parser with real files.
"""
import pytest
import tempfile
import os
from src.testkit_indexer.parser import CSharpParser
from tests.factories import create_testkit_class_code


class TestParserIntegration:
    """Integration tests for C# parser."""

    def setup_method(self):
        """Set up test fixtures."""
        self.parser = CSharpParser()

    def test_parse_real_csharp_file(self):
        """Test parsing a real C# file with methods and tags."""
        # Given
        csharp_code = create_testkit_class_code()
        
        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.cs', delete=False) as f:
            f.write(csharp_code)
            temp_file = f.name

        try:
            # When
            result = self.parser.parse_file(temp_file)
            
            # Then
            assert result.success is True
            assert result.method_count == 3
            assert result.tag_count == 6  # factory, test-data, helper, user, message, telegram, generic
            
            # Check first method
            create_user = result.methods[0]
            assert create_user.name == "CreateUser"
            assert create_user.tags == ["user", "factory", "test-data"]
            assert create_user.is_static is True
            assert create_user.return_type == "User"
            
            # Check second method
            create_message = result.methods[1]
            assert create_message.name == "CreateMessage"
            assert create_message.tags == ["message", "factory", "telegram"]
            
            # Check generic method
            create_factory = result.methods[2]
            assert create_factory.name == "CreateFactory"
            assert create_factory.tags == ["factory", "generic"]
            assert create_factory.is_generic is True
            
        finally:
            # Clean up
            os.unlink(temp_file)

    def test_parse_file_with_errors(self):
        """Test parsing a file with syntax errors."""
        # Given
        malformed_code = '''
        public class TestHelper {
            public static Message CreateMessage() {
                // Missing closing brace
        '''
        
        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.cs', delete=False) as f:
            f.write(malformed_code)
            temp_file = f.name

        try:
            # When
            result = self.parser.parse_file(temp_file)
            
            # Then
            # Should not crash, but may return empty results
            assert isinstance(result.methods, list)
            assert result.file_path == temp_file
            
        finally:
            # Clean up
            os.unlink(temp_file)

    def test_parse_nonexistent_file(self):
        """Test parsing a non-existent file."""
        # When
        result = self.parser.parse_file("/nonexistent/file.cs")
        
        # Then
        assert result.success is False
        assert len(result.errors) > 0
        assert result.method_count == 0 