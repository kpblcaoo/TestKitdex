"""
Unit tests for database functionality.
"""
import pytest
from unittest.mock import Mock, patch
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Test database setup
@pytest.fixture
def test_engine():
    """Create test database engine."""
    return create_engine("sqlite:///:memory:")

@pytest.fixture
def test_session(test_engine):
    """Create test database session."""
    Session = sessionmaker(bind=test_engine)
    session = Session()
    yield session
    session.close()

@pytest.fixture
def mock_user():
    """Create mock user for testing."""
    from testkitdex.data.testkit_sample.factories import create_user_factory, create_message_factory
    return create_user_factory() 