"""
Unit tests for database functionality using TestKit.
"""
import pytest
import tempfile
import os
import sys

# Добавляем корень проекта в путь
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from src.testkit_indexer.database import TestKitRepository, Method
from src.testkit_indexer.parser.models import CSharpMethod
from data.testkit_sample.factories import create_user_factory, create_message_factory


class TestDatabase:
    """Test database functionality using TestKit."""
    
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
        """Test storing method with tags using TestKit."""
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
        user_method = create_user_factory()
        message_method = create_message_factory()
        self.repository.store_method(user_method)
        self.repository.store_method(message_method)
        
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
        user_method = create_user_factory()
        message_method = create_message_factory()
        self.repository.store_method(user_method)
        self.repository.store_method(message_method)
        
        # When
        all_tags = self.repository.get_all_tags()
        
        # Then
        assert len(all_tags) >= 5  # user, factory, test-data, message, telegram
        tag_names = [tag.name for tag in all_tags]
        assert "user" in tag_names
        assert "factory" in tag_names
        assert "message" in tag_names
    
    @pytest.mark.skip(reason="Statistics format needs to be clarified")
    def test_get_statistics(self):
        """Test retrieving database statistics."""
        # Given
        user_method = create_user_factory()
        message_method = create_message_factory()
        self.repository.store_method(user_method)
        self.repository.store_method(message_method)
        
        # When
        stats = self.repository.get_statistics()
        
        # Then
        # stats может быть dict или объект, проверяем оба варианта
        if isinstance(stats, dict):
            assert stats["total_methods"] == 2
            assert stats["total_tags"] >= 5
            assert stats["methods_with_tags"] == 2
            assert stats["methods_without_tags"] == 0
        else:
            assert stats.total_methods == 2
            assert stats.total_tags >= 5
            assert stats.methods_with_tags == 2
            assert stats.methods_without_tags == 0
    
    @pytest.mark.skip(reason="FTS5 search needs to be implemented")
    def test_search_methods(self):
        """Test searching methods using full-text search."""
        # Given
        user_method = create_user_factory()
        message_method = create_message_factory()
        self.repository.store_method(user_method)
        self.repository.store_method(message_method)
        
        # When
        search_results = self.repository.search_methods("Create")
        
        # Then
        assert len(search_results) == 2
        method_names = [m.name for m in search_results]
        assert "CreateUser" in method_names
        assert "CreateMessage" in method_names
    
    def test_duplicate_tags_handling(self):
        """Test handling duplicate tags gracefully."""
        # Given
        method1 = create_user_factory()
        method2 = create_message_factory()
        
        # When
        stored_method1 = self.repository.store_method(method1)
        stored_method2 = self.repository.store_method(method2)
        
        # Then
        # Both methods should have "factory" tag without conflicts
        with self.repository.get_session() as session:
            method1_tags = session.query(Method).filter(Method.id == stored_method1.id).first().tags
            method2_tags = session.query(Method).filter(Method.id == stored_method2.id).first().tags
            
            factory_tags1 = [tag.name for tag in method1_tags if tag.name == "factory"]
            factory_tags2 = [tag.name for tag in method2_tags if tag.name == "factory"]
            
            assert len(factory_tags1) == 1
            assert len(factory_tags2) == 1 