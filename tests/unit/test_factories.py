"""
Tests for TestKit factories using factory-boy.
"""
import pytest
import sys
import os

# Добавляем корень проекта в путь
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from data.testkit_sample.factories import (
    CSharpMethodFactory,
    CSharpCodeFactory,
    create_user_factory,
    create_message_factory,
    create_generic_factory,
    create_user_factory_code,
    create_message_factory_code,
    create_generic_factory_code,
    create_testkit_class_code
)


class TestCSharpMethodFactory:
    """Test C# method factory using factory-boy."""
    
    def test_create_user_factory_method(self):
        """Test creating user factory method."""
        # When
        method = create_user_factory()
        
        # Then
        assert method.name == "CreateUser"
        assert method.return_type == "User"
        assert method.tags == ["user", "factory", "test-data"]
        assert method.is_static is True
        assert method.parameters == ["string name = \"TestUser\""]
    
    def test_create_message_factory_method(self):
        """Test creating message factory method."""
        # When
        method = create_message_factory()
        
        # Then
        assert method.name == "CreateMessage"
        assert method.return_type == "Message"
        assert method.tags == ["message", "factory", "telegram"]
        assert method.is_static is True
        assert method.parameters == ["string text = \"Test message\""]
    
    def test_create_generic_factory_method(self):
        """Test creating generic factory method."""
        # When
        method = create_generic_factory()
        
        # Then
        assert method.name == "CreateFactory"
        assert method.return_type == "T"
        assert method.tags == ["factory", "generic"]
        assert method.is_generic is True
        assert method.is_static is True
    
    def test_create_custom_method(self):
        """Test creating custom method with factory-boy."""
        # When
        method = CSharpMethodFactory.create(
            name="CustomMethod",
            return_type="string",
            parameters=["int id", "string name"],
            tags=["custom", "test"],
            summary="Custom test method",
            is_static=False
        )
        
        # Then
        assert method.name == "CustomMethod"
        assert method.return_type == "string"
        assert method.tags == ["custom", "test"]
        assert method.is_static is False
        assert method.parameters == ["int id", "string name"]
    
    def test_factory_boy_auto_generation(self):
        """Test factory-boy automatic data generation."""
        # When
        method = CSharpMethodFactory()
        
        # Then
        assert method.name is not None
        assert method.return_type is not None
        assert isinstance(method.tags, list)
        assert isinstance(method.is_static, bool)
        assert isinstance(method.is_generic, bool)


class TestCSharpCodeFactory:
    """Test C# code factory using factory-boy."""
    
    def test_create_user_factory_code(self):
        """Test creating user factory code."""
        # When
        code = create_user_factory_code()
        
        # Then
        assert "CreateUser" in code
        assert "User" in code
        assert "user, factory, test-data" in code
        assert "public static" in code
    
    def test_create_message_factory_code(self):
        """Test creating message factory code."""
        # When
        code = create_message_factory_code()
        
        # Then
        assert "CreateMessage" in code
        assert "Message" in code
        assert "message, factory, telegram" in code
        assert "public static" in code
    
    def test_create_generic_factory_code(self):
        """Test creating generic factory code."""
        # When
        code = create_generic_factory_code()
        
        # Then
        assert "CreateFactory" in code
        assert "T" in code
        assert "factory, generic" in code
        assert "public static" in code
    
    def test_create_testkit_class_code(self):
        """Test creating TestKit class code."""
        # When
        code = create_testkit_class_code()
        
        # Then
        assert "class TestKit" in code
        assert "CreateUser" in code
        assert "CreateMessage" in code
        assert "CreateFactory" in code
        assert "user, factory, test-data" in code
        assert "message, factory, telegram" in code
        assert "factory, generic" in code


class TestFactoryIntegration:
    """Test integration between factories."""
    
    @pytest.mark.skip(reason="Parser tags extraction not fully implemented")
    def test_parse_factory_generated_code(self, csharp_parser):
        """Test parsing factory generated code."""
        # Given
        code = create_user_factory_code()
        
        # When
        methods = csharp_parser.extract_methods(code)
        
        # Then
        assert len(methods) == 1
        method = methods[0]
        assert method.name == "CreateUser"
        assert method.tags == ["user", "factory", "test-data"]
        assert method.is_static is True
    
    def test_factory_boy_batch_creation(self):
        """Test creating multiple methods with factory-boy."""
        # When
        methods = CSharpMethodFactory.create_batch(3)
        
        # Then
        assert len(methods) == 3
        for method in methods:
            assert method.name is not None
            assert method.return_type is not None
            assert isinstance(method.tags, list)
    
    def test_factory_boy_with_override(self):
        """Test factory-boy with parameter override."""
        # When
        method = CSharpMethodFactory.create(
            name="OverrideMethod",
            tags=["override", "test"]
        )
        
        # Then
        assert method.name == "OverrideMethod"
        assert method.tags == ["override", "test"]
        assert method.return_type is not None  # Auto-generated 