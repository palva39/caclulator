# Remove the erroneous code from `commands.py`
clean_plugin_loader_code = """
import importlib
import os
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class PluginLoader:
    def __init__(self, plugin_directory):
        self.plugin_directory = plugin_directory
        self.commands = {}

    def load_plugins(self):
        # Iterate over files in the plugin directory
        for filename in os.listdir(self.plugin_directory):
            if filename.endswith('.py') and filename != '__init__.py':
                # Import the module dynamically
                module_name = filename[:-3]
                module = importlib.import_module(f'calculator.plugins.{module_name}')
                # Register all commands from the plugin
                for attr in dir(module):
                    cls = getattr(module, attr)
                    if isinstance(cls, type) and issubclass(cls, Command) and cls is not Command:
                        self.commands[cls.__name__] = cls()

    def get_command(self, command_name):
        return self.commands.get(command_name)
"""

# Write the corrected code to `commands.py`
with open(commands_file_path, 'w') as file:
    file.write(clean_plugin_loader_code)

# Confirm the fix has been applied successfully
commands_file_path
