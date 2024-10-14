"""
Unit tests for commands.py module.
This module tests the functionality of the calculator commands (add, subtract, multiply, divide).
"""

import pytest
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    """Test the AddCommand functionality."""
    command = AddCommand()
    assert command.execute(2, 3) == 5
    assert command.execute(-1, 1) == 0

def test_subtract_command():
    """Test the SubtractCommand functionality."""
    command = SubtractCommand()
    assert command.execute(5, 3) == 2
    assert command.execute(0, 5) == -5

def test_multiply_command():
    """Test the MultiplyCommand functionality."""
    command = MultiplyCommand()
    assert command.execute(2, 3) == 6
    assert command.execute(-1, 3) == -3

def test_divide_command():
    """Test the DivideCommand functionality, including division by zero."""
    command = DivideCommand()
    assert command.execute(6, 3) == 2
    assert command.execute(5, 2) == 2.5

    with pytest.raises(ValueError):
        command.execute(5, 0)
