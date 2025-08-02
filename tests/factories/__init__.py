"""
Test factories - Backward compatibility layer
Импортирует из нового TestKit для обратной совместимости
"""

import os
import sys

# Добавляем корень проекта в путь
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Импортируем из нового TestKit
from data.testkit_sample.factories import (
    CSharpMethodFactory,
    CSharpCodeFactory,
    create_user_factory,
    create_message_factory,
    create_generic_factory,
    create_validation_method,
    create_simple_method,
    create_user_factory_code,
    create_message_factory_code,
    create_generic_factory_code,
    create_simple_method_code,
    create_testkit_class_code
)

__all__ = [
    'CSharpMethodFactory',
    'CSharpCodeFactory',
    'create_user_factory',
    'create_message_factory',
    'create_generic_factory',
    'create_validation_method',
    'create_simple_method',
    'create_user_factory_code',
    'create_message_factory_code',
    'create_generic_factory_code',
    'create_simple_method_code',
    'create_testkit_class_code'
] 