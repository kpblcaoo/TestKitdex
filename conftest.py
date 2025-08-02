"""
Pytest configuration for TestKit project
"""

import os
import sys

# Добавляем корень проекта в PYTHONPATH
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root) 