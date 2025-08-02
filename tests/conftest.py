"""
Pytest configuration for TestKit tests
"""

import pytest

@pytest.fixture
def csharp_parser():
    """C# parser fixture."""
    from testkitdex.testkit_indexer.parser import CSharpParser
    return CSharpParser() 