"""
Unit tests for database functionality.
"""
import pytest
import tempfile
import os
from src.testkit_indexer.database import TestKitRepository, Method
from src.testkit_indexer.parser.models import CSharpMethod
from tests.factories import create_user_factory, create_message_factory


class TestDatabase:
    """Test database functionality."""
    
    def setup_method(self):
        """Set up test fixtures."""
        # Create temporary database
        self.temp_db = tempfile.NamedTemporaryFile(suffix='.db', delete=False)
        self.db_url = f"sqlite:///{self.temp_db.name}"
        self.repository = TestKitRepository(self.db_url)
        self.repository.create_tables()
    
    def teardown_method(self):
        """Clean up test fixtures."""
        self.temp_db.close()
        os.unlink(self.temp_db.name)
    
    def test_store_method_with_tags(self):
        """Test storing method with tags."""
        # Given
        method = create_user_factory()
        
        # When
        stored_method = self.repository.store_method(method)
        
        # Then
        assert stored_method.name == "CreateUser"
        assert stored_method.return_type == "User"
        
        # Get tags in a new session
        with self.repository.get_session() as session:
            method_with_tags = session.query(Method).filter(Method.id == stored_method.id).first()
            assert len(method_with_tags.tags) == 3
            tag_names = [tag.name for tag in method_with_tags.tags]
            assert "user" in tag_names
            assert "factory" in tag_names
            assert "test-data" in tag_names
    
    def test_get_method_by_name(self):
        """Test retrieving method by name."""
        # Given
        method = create_user_factory()
        self.repository.store_method(method)
        
        # When
        retrieved_method = self.repository.get_method_by_name("CreateUser")
        
        # Then
        assert retrieved_method is not None
        assert retrieved_method.name == "CreateUser"
        assert retrieved_method.return_type == "User"
    
    def test_get_methods_by_tags(self):
        """Test retrieving methods by tags."""
        # Given
        user_method = create_user_factory()
        message_method = create_message_factory()
        self.repository.store_method(user_method)
        self.repository.store_method(message_method)
        
        # When
        factory_methods = self.repository.get_methods_by_tags(["factory"])
        
        # Then
        assert len(factory_methods) == 2
        method_names = [m.name for m in factory_methods]
        assert "CreateUser" in method_names
        assert "CreateMessage" in method_names
    
    def test_store_method_with_parameters(self):
        """Test storing method with parameters."""
        # Given
        method = CSharpMethod(
            name="TestMethod",
            return_type="string",
            parameters=["int id", "string name = \"default\""],
            tags=["test"],
            summary="Test method with parameters"
        )
        
        # When
        stored_method = self.repository.store_method(method)
        
        # Then
        # Get parameters in a new session
        with self.repository.get_session() as session:
            method_with_params = session.query(Method).filter(Method.id == stored_method.id).first()
            assert len(method_with_params.parameters) == 2
            
            param1 = method_with_params.parameters[0]
            assert param1.name == "id"
            assert param1.type == "int"
            assert param1.default_value is None
            
            param2 = method_with_params.parameters[1]
            assert param2.name == "name"
            assert param2.type == "string"
            assert param2.default_value == "default"
    
    def test_get_all_methods(self):
        """Test retrieving all methods."""
        # Given
        method1 = create_user_factory()
        method2 = create_message_factory()
        self.repository.store_method(method1)
        self.repository.store_method(method2)
        
        # When
        all_methods = self.repository.get_all_methods()
        
        # Then
        assert len(all_methods) == 2
        method_names = [m.name for m in all_methods]
        assert "CreateUser" in method_names
        assert "CreateMessage" in method_names
    
    def test_get_all_tags(self):
        """Test retrieving all tags."""
        # Given
        method1 = create_user_factory()
        method2 = create_message_factory()
        self.repository.store_method(method1)
        self.repository.store_method(method2)
        
        # When
        all_tags = self.repository.get_all_tags()
        
        # Then
        assert len(all_tags) >= 5  # user, factory, test-data, message, telegram
        tag_names = [tag.name for tag in all_tags]
        assert "user" in tag_names
        assert "factory" in tag_names
        assert "message" in tag_names
    
    def test_get_statistics(self):
        """Test getting database statistics."""
        # Given
        method1 = create_user_factory()
        method2 = create_message_factory()
        self.repository.store_method(method1)
        self.repository.store_method(method2)
        
        # When
        stats = self.repository.get_statistics()
        
        # Then
        assert stats["method_count"] == 2
        assert stats["tag_count"] >= 5
        assert stats["parameter_count"] == 2  # Both methods have 1 parameter each
        assert len(stats["top_tags"]) > 0
        assert any(tag["name"] == "factory" for tag in stats["top_tags"])
    
    @pytest.mark.skip(reason="FTS5 search needs to be implemented")
    def test_search_methods(self):
        """Test searching methods using FTS5."""
        # Given
        method1 = create_user_factory()
        method2 = create_message_factory()
        self.repository.store_method(method1)
        self.repository.store_method(method2)
        self.repository.update_search_index()
        
        # When
        user_results = self.repository.search_methods("user")
        factory_results = self.repository.search_methods("factory")
        
        # Then
        assert len(user_results) == 1
        assert user_results[0].name == "CreateUser"
        
        assert len(factory_results) == 2
        method_names = [m.name for m in factory_results]
        assert "CreateUser" in method_names
        assert "CreateMessage" in method_names
    
    def test_duplicate_tags_handling(self):
        """Test that duplicate tags are handled correctly."""
        # Given
        method1 = create_user_factory()
        method2 = create_message_factory()
        
        # When
        self.repository.store_method(method1)
        self.repository.store_method(method2)
        
        # Then
        all_tags = self.repository.get_all_tags()
        tag_names = [tag.name for tag in all_tags]
        
        # Check that "factory" tag exists only once
        factory_tags = [tag for tag in all_tags if tag.name == "factory"]
        assert len(factory_tags) == 1
        
        # Check that both methods have the factory tag
        factory_methods = self.repository.get_methods_by_tags(["factory"])
        assert len(factory_methods) == 2 