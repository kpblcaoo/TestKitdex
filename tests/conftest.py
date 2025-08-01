"""
Pytest configuration
"""
import pytest
# from data.testkit_sample import TK
# from data.testkit_sample.di import container

# Глобальные фикстуры
# @pytest.fixture(scope="session")
# def testkit():
#     """Глобальный TestKit"""
#     return TK

# @pytest.fixture(scope="function")
# def di_container():
#     """DI контейнер для каждого теста"""
#     container.clear()
#     yield container

@pytest.fixture
def csharp_parser():
    """C# parser fixture."""
    from src.testkit_indexer.parser import CSharpParser
    return CSharpParser() 