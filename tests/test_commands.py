# tests/test_commands.py
import pytest
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    command = AddCommand()
    assert command.execute(2, 3) == 5
    assert command.execute(-1, 1) == 0

def test_subtract_command():
    command = SubtractCommand()
    assert command.execute(5, 3) == 2
    assert command.execute(0, 5) == -5

def test_multiply_command():
    command = MultiplyCommand()
    assert command.execute(2, 3) == 6
    assert command.execute(-1, 3) == -3

def test_divide_command():
    command = DivideCommand()
    assert command.execute(6, 3) == 2
    assert command.execute(5, 2) == 2.5

    with pytest.raises(ValueError):
        command.execute(5, 0)
