"""
Common step definitions for TestKit BDD scenarios
Универсальные step definitions с параметризованными шагами
"""

# Импорты из модулей common
from features.steps.common.steps.given_steps import *
from features.steps.common.steps.when_steps import *
from features.steps.common.steps.then_steps import *

# Экспортируем все step definitions
__all__ = [
    # Given steps
    'step_impl as given_step_impl',
    # When steps
    'step_impl as when_step_impl', 
    # Then steps
    'step_impl as then_step_impl'
] 