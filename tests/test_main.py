# tests/test_main.py
import sys
import os
import pytest
from unittest import mock
from main import parse_command

# Tests for parse_command function
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

# Tests for REPL function with mocked input
def test_repl_add_command():
    inputs = iter(["add 2 3", "exit"])
    with mock.patch('builtins.input', lambda _: next(inputs)):
        with mock.patch('builtins.print') as mocked_print:
            repl()
            mocked_print.assert_any_call("Result: 5.0")

def test_repl_invalid_command():
    inputs = iter(["invalid 5 2", "exit"])
    with mock.patch('builtins.input', lambda _: next(inputs)):
        with mock.patch('builtins.print') as mocked_print:
            repl()
            mocked_print.assert_any_call("Error: Unknown command: invalid")

def test_repl_invalid_format():
    inputs = iter(["add 2", "exit"])  # missing second argument
    with mock.patch('builtins.input', lambda _: next(inputs)):
        with mock.patch('builtins.print') as mocked_print:
            repl()
            mocked_print.assert_any_call("Error: Invalid input format. Use: <command> <num1> <num2>")

def test_repl_divide_by_zero():
    inputs = iter(["divide 5 0", "exit"])
    with mock.patch('builtins.input', lambda _: next(inputs)):
        with mock.patch('builtins.print') as mocked_print:
            repl()
            mocked_print.assert_any_call("Error: Cannot divide by zero")

def test_repl_exit():
    inputs = iter(["exit"])
    with mock.patch('builtins.input', lambda _: next(inputs)):
        with mock.patch('builtins.print') as mocked_print:
            repl()
            mocked_print.assert_any_call("Goodbye!")