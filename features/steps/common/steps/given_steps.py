"""
Given step definitions for TestKit BDD scenarios
Given шаги для BDD сценариев TestKit
"""

from unittest.mock import Mock
from behave import given
from features.steps.common import dispatch


@given("I have {data_type} with {condition}")
def step_impl(context, data_type, condition):
    """Универсальный шаг для создания данных с условием"""
    # Используем диспетчеризацию для создания данных
    builder = create_bdd_data()
    builder = dispatch(builder, f"{data_type} with {condition}")
    context.test_data = builder.build()


@given("I have {data_type} data")
def step_impl(context, data_type):
    """Упрощенный шаг для создания данных без условий"""
    # Используем диспетчеризацию для создания данных
    builder = create_bdd_data()
    builder = dispatch(builder, data_type)
    context.test_data = builder.build()


# Специфичные шаги для Background секции
@given("I have a clean database")
def step_impl(context):
    """Setup clean database for tests"""
    context.db_path = "/tmp/testkit_test.db"
    context.indexed_methods = 0
    context.previous_count = 0


@given("I have a TestKit directory")
def step_impl(context):
    """Setup TestKit directory for tests"""
    context.testkit_dir = "/tmp/testkit_sample"
    context.indexed_methods = 0


def create_bdd_data():
    """Создание BDD builder"""
    try:
        from testkitdex.data.testkit_sample.builders.bdd_builders import create_bdd_data
        return create_bdd_data()
    except ImportError:
        # Fallback для тестов
        return Mock() 