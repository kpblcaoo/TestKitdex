"""
Factory for creating C# methods in tests.
"""
from typing import List, Optional
from src.testkit_indexer.parser.models import CSharpMethod


class CSharpMethodFactory:
    """Factory for creating C# methods in tests."""
    
    @staticmethod
    def create_method(
        name: str = "TestMethod",
        return_type: str = "void",
        parameters: Optional[List[str]] = None,
        tags: Optional[List[str]] = None,
        summary: Optional[str] = None,
        is_static: bool = False,
        is_generic: bool = False,
        is_public: bool = True,
        file_path: Optional[str] = None,
        line_number: Optional[int] = None
    ) -> CSharpMethod:
        """Create a C# method for testing."""
        if parameters is None:
            parameters = []
        if tags is None:
            tags = []
            
        return CSharpMethod(
            name=name,
            return_type=return_type,
            parameters=parameters,
            tags=tags,
            summary=summary,
            is_static=is_static,
            is_generic=is_generic,
            is_public=is_public,
            file_path=file_path,
            line_number=line_number
        )
    
    @staticmethod
    def create_user_factory_method() -> CSharpMethod:
        """Create a user factory method."""
        return CSharpMethodFactory.create_method(
            name="CreateUser",
            return_type="User",
            parameters=["string name = \"TestUser\""],
            tags=["user", "factory", "test-data"],
            summary="Creates a test user",
            is_static=True,
            is_public=True
        )
    
    @staticmethod
    def create_message_factory_method() -> CSharpMethod:
        """Create a message factory method."""
        return CSharpMethodFactory.create_method(
            name="CreateMessage",
            return_type="Message",
            parameters=["string text = \"Test message\""],
            tags=["message", "factory", "telegram"],
            summary="Creates a test message",
            is_static=True,
            is_public=True
        )
    
    @staticmethod
    def create_generic_factory_method() -> CSharpMethod:
        """Create a generic factory method."""
        return CSharpMethodFactory.create_method(
            name="CreateFactory",
            return_type="T",
            parameters=[],
            tags=["factory", "generic"],
            summary="Generic factory method",
            is_static=True,
            is_generic=True,
            is_public=True
        )
    
    @staticmethod
    def create_validation_method() -> CSharpMethod:
        """Create a validation method."""
        return CSharpMethodFactory.create_method(
            name="ValidateUser",
            return_type="bool",
            parameters=["User user"],
            tags=["validation", "user"],
            summary="Validates user data",
            is_static=False,
            is_public=True
        )
    
    @staticmethod
    def create_simple_method() -> CSharpMethod:
        """Create a simple method without tags."""
        return CSharpMethodFactory.create_method(
            name="DoSomething",
            return_type="void",
            parameters=[],
            tags=[],
            summary=None,
            is_static=False,
            is_public=True
        )


# Convenience functions
def create_user_factory() -> CSharpMethod:
    """Create a user factory method."""
    return CSharpMethodFactory.create_user_factory_method()


def create_message_factory() -> CSharpMethod:
    """Create a message factory method."""
    return CSharpMethodFactory.create_message_factory_method()


def create_generic_factory() -> CSharpMethod:
    """Create a generic factory method."""
    return CSharpMethodFactory.create_generic_factory_method()


def create_validation_method() -> CSharpMethod:
    """Create a validation method."""
    return CSharpMethodFactory.create_validation_method()


def create_simple_method() -> CSharpMethod:
    """Create a simple method."""
    return CSharpMethodFactory.create_simple_method() 