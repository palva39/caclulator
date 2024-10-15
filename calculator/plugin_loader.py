# First, let's create a `plugins` directory inside the `calculator` directory for future plugins

plugins_dir = os.path.join(calculator_dir, 'plugins')
os.makedirs(plugins_dir, exist_ok=True)

# Now, let's create a basic plugin loader that will dynamically load all plugins from this folder
plugin_loader_content = '''
import os
import importlib

class PluginLoader:
    def __init__(self, plugins_path):
        self.plugins_path = plugins_path
        self.commands = {}

    def load_plugins(self):
        # Dynamically load all Python files in the plugins directory
        for filename in os.listdir(self.plugins_path):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = f"calculator.plugins.{filename[:-3]}"
                module = importlib.import_module(module_name)
                
                # Expect each plugin to have a `register` function that registers the command
                if hasattr(module, "register"):
                    command_name, command_class = module.register()
                    self.commands[command_name] = command_class

    def get_command(self, command_name):
        return self.commands.get(command_name, None)
'''

# Write this plugin loader to the calculator directory
plugin_loader_file_path = os.path.join(calculator_dir, 'plugin_loader.py')

with open(plugin_loader_file_path, 'w') as file:
    file.write(plugin_loader_content)

plugin_loader_file_path
