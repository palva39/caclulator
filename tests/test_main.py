import pytest
from unittest import mock
from main import repl, parse_command

# Test the command parsing logic (already present)
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

# Mock the input and print functions to simulate REPL interaction
def test_repl_add_command():
    user_inputs = ['add 2 3', 'exit']
    with mock.patch('builtins.input', side_effect=user_inputs):
        with mock.patch('builtins.print') as mock_print:
            repl()

    mock_print.assert_any_call("Result: 5")
    mock_print.assert_any_call("Goodbye!")

def test_repl_subtract_command():
    user_inputs = ['subtract 5 3', 'exit']
    with mock.patch('builtins.input', side_effect=user_inputs):
        with mock.patch('builtins.print') as mock_print:
            repl()

    mock_print.assert_any_call("Result: 2")
    mock_print.assert_any_call("Goodbye!")

def test_repl_invalid_command():
    user_inputs = ['invalid_command 1 2', 'exit']
    with mock.patch('builtins.input', side_effect=user_inputs):
        with mock.patch('builtins.print') as mock_print:
            repl()

    mock_print.assert_any_call("Error: Unknown command: invalid_command")

def test_repl_divide_by_zero():
    user_inputs = ['divide 4 0', 'exit']
    with mock.patch('builtins.input', side_effect=user_inputs):
        with mock.patch('builtins.print') as mock_print:
            repl()

    mock_print.assert_any_call("Error: Cannot divide by zero")
    