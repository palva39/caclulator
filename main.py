# main.py
import os
import logging
import logging.config
from calculator.commands import PluginLoader

# Calculate the actual file system path to the 'plugins' directory
plugin_directory = os.path.join(os.path.dirname(__file__), 'calculator', 'plugins')

# Initialize the PluginLoader with the correct path
plugin_loader = PluginLoader(plugin_directory)
plugin_loader.load_plugins()

def parse_command(input_str):
    """Parse the user input to identify the command and its arguments."""
    parts = input_str.strip().split()
    if len(parts) < 3:
        raise ValueError("Invalid input format. Use: <command> <num1> <num2>")

    command_str = parts[0]
    try:
        num1 = float(parts[1])
        num2 = float(parts[2])
    except ValueError:
        raise ValueError("Invalid numbers provided.")

    # Use the plugin loader to get the command dynamically
    command_class = plugin_loader.get_command(command_str.capitalize() + 'Command')
    if command_class:
        return command_class, num1, num2
    else:
        raise ValueError(f"Unknown command: {command_str}")

def repl():
    """Start the REPL loop."""
    print("Welcome to the interactive calculator!")
    print("Available commands:", ', '.join([cmd[:-7].lower() for cmd in plugin_loader.commands.keys()]))
    print("Usage: <command> <num1> <num2> (example: add 2 3)")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("Enter command: ")
        if user_input.strip().lower() == 'exit':
            print("Goodbye!")
            break

        try:
            command, num1, num2 = parse_command(user_input)
            result = command.execute(num1, num2)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()

"""Load the logging configuration from logging.conf"""
logging.config.fileConfig('logging.conf')

# Create a logger
logger = logging.getLogger(__name__)

def main():
    # Example log messages
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")

    print("Running the main application...")

if __name__ == "__main__":
    main()
