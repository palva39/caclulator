"""
Unit tests for PluginLoader in commands.py module.
This module tests the functionality of dynamically loading 
calculator commands (add, subtract, multiply, divide).
"""
from calculator.commands import PluginLoader
import pytest
import os

# Initialize the plugin loader for the tests
plugin_directory = os.path.join(os.path.dirname(__file__), '../calculator/plugins')
plugin_loader = PluginLoader(plugin_directory)
plugin_loader.load_plugins()

def test_add_command():
    """Test the AddCommand functionality loaded via PluginLoader."""
    command = plugin_loader.get_command('AddCommand')
    assert command.execute(2, 3) == 5
    assert command.execute(-1, 1) == 0

def test_subtract_command():
    """Test the SubtractCommand functionality loaded via PluginLoader."""
    command = plugin_loader.get_command('SubtractCommand')
    assert command.execute(5, 3) == 2
    assert command.execute(0, 5) == -5

def test_multiply_command():
    """Test the MultiplyCommand functionality loaded via PluginLoader."""
    command = plugin_loader.get_command('MultiplyCommand')
    assert command.execute(2, 3) == 6
    assert command.execute(-1, 3) == -3

def test_divide_command():
    """Test the DivideCommand functionality, including division by zero, loaded via PluginLoader."""
    command = plugin_loader.get_command('DivideCommand')
    assert command.execute(6, 3) == 2
    assert command.execute(5, 2) == 2.5

    with pytest.raises(ValueError):
        command.execute(5, 0)

def test_add_command_invalid_input():
    """Test AddCommand with invalid inputs loaded via PluginLoader."""
    command = plugin_loader.get_command('AddCommand')
    with pytest.raises(TypeError):
        command.execute("a", 3)

def test_subtract_command_invalid_input():
    """Test SubtractCommand with invalid inputs loaded via PluginLoader."""
    command = plugin_loader.get_command('SubtractCommand')
    with pytest.raises(TypeError):
        command.execute("a", "b")
