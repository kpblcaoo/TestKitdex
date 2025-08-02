"""
TestKit Generators
"""

from .scenario_generator import TestScenarioGenerator

# Глобальный экземпляр
scenario_generator = TestScenarioGenerator()

# Удобные функции
def create_simple_scenario():
    """Создать простой сценарий"""
    return scenario_generator.create_simple_scenario()

def create_complex_scenario():
    """Создать сложный сценарий"""
    return scenario_generator.create_complex_scenario()

def create_performance_scenario(user_count: int = 10, message_count: int = 50):
    """Создать сценарий производительности"""
    return scenario_generator.create_performance_scenario(user_count, message_count)

def create_error_scenario():
    """Создать сценарий с ошибками"""
    return scenario_generator.create_error_scenario()

def create_custom_scenario(**kwargs):
    """Создать кастомный сценарий"""
    return scenario_generator.create_custom_scenario(**kwargs)

__all__ = [
    'TestScenarioGenerator',
    'scenario_generator',
    'create_simple_scenario',
    'create_complex_scenario', 
    'create_performance_scenario',
    'create_error_scenario',
    'create_custom_scenario'
] 