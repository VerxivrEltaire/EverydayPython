# user_script.py
import example_module

# Global variable in the user's script
user_variable = "I am a user variable"

# Function in the user's script
def user_function():
    print("I am a function in the user's script")

# Accessing the module's name using __name__
print(f"Imported module name: {example_module.__name__}")
# Output: Imported module name: example_module

# Accessing module-level variable from user script
print(f"Module variable from user script: {example_module.module_variable}")
# Output: Module variable from user script: I am a module variable

# Calling module-level function from user script
example_module.module_function()  # Output: I am a function within the module

# Calling user-level function
user_function()  # Output: I am a function in the user's script
