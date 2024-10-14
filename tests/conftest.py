"""
This module sets up pytest configuration, including dynamic test generation
using Faker and providing custom test data for calculator tests.
"""
# conftest.py
from decimal import Decimal
import pytest # pylint: disable=unused-import
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    """
    Generate test data with random numbers and operations.

    :param num_records: Number of test records to generate
    :yield: A tuple containing operands, operation name, operation function, and expected result
    """
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    # Generate test data
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else (
            Decimal(fake.random_number(digits=1)))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        if operation_func is divide and b == Decimal('0'):
            b = Decimal('1') # Avoid division by zero by setting b to 1

        try:
            expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """
    Add a command-line option to specify the number of records for test generation.
    """
    parser.addoption("--num_records", action="store", default=5,
                     type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """
    Generate dynamic tests based on the number of records 
    specified through the --num_records option.
    """
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        modified_parameters = [
            (a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected)
                               for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)

# Assuming you have fixture setup in conftest.py
def test_fixture_setup(fixture_name):
    """Test that the fixture is set up correctly."""
    assert fixture_name is not None
