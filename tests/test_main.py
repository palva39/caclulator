# tests/test_main.py
import pytest
from main import parse_command

def test_parse_command_add():
    command, num1, num2 = parse_command("add 2 3")
    assert command.execute(num1, num2) == 5

def test_parse_command_subtract():
    command, num1, num2 = parse_command("subtract 5 2")
    assert command.execute(num1, num2) == 3

def test_parse_command_multiply():
    command, num1, num2 = parse_command("multiply 3 4")
    assert command.execute(num1, num2) == 12

def test_parse_command_divide():
    command, num1, num2 = parse_command("divide 10 2")
    assert command.execute(num1, num2) == 5

    with pytest.raises(ValueError):
        command, num1, num2 = parse_command("divide 5 0")
        command.execute(num1, num2)

def test_invalid_command():
    with pytest.raises(ValueError):
        parse_command("invalid 5 2")
