"""
Pytest configuration for TestKit project
"""

import os
import sys

print("=== CONFTEST.PY LOADED ===")
print(f"Current working directory: {os.getcwd()}")
print(f"sys.path before: {sys.path[:3]}")

# Добавляем текущую директорию в самое начало пути
current_dir = os.getcwd()
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Добавляем корень проекта в PYTHONPATH
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Также добавляем src директорию для импорта модулей из src
src_path = os.path.join(project_root, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

print(f"sys.path after: {sys.path[:3]}")
print("=== CONFTEST.PY END ===") 