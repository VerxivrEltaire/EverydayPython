# example_module.py

# Module-level global variable
module_variable = "I am a module variable"

# Module-level function
def module_function():
    print("I am a function within the module")

# Accessing the module's name using __name__
print(f"Module name: {__name__}")

# Execution of the module-level code
if __name__ == "__main__":
    print("This code runs only when the module is executed directly.")
