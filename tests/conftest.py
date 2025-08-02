"""
Pytest configuration for TestKit tests
"""

import os
import sys
import pathlib

print("=== TESTS/CONFTEST.PY LOADED ===")
print(f"Current working directory: {os.getcwd()}")
print(f"sys.path before: {sys.path[:3]}")

# Надежное решение: добавляем корень проекта в самое начало пути
project_root = str(pathlib.Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Добавляем родительскую директорию в самое начало пути
parent_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Добавляем текущую директорию в самое начало пути
current_dir = os.getcwd()
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Добавляем корень проекта в PYTHONPATH
project_root_alt = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root_alt not in sys.path:
    sys.path.insert(0, project_root_alt)

# Также добавляем src директорию для импорта модулей из src
src_path = os.path.join(project_root, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

print(f"sys.path after: {sys.path[:3]}")
print("=== TESTS/CONFTEST.PY END ===")

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