# Basic documentation string
def greet(name):
    """This function greets the person passed in as a parameter."""
    return f'Hello, {name}!'

# Detailed documentation string
def power(base, exponent):
    """
    Calculate the power of a number.

    Args:
        base (int or float): The base number.
        exponent (int): The exponent to raise the base to.

    Returns:
        int or float: The result of base raised to the exponent.
    """
    return base ** exponent


# Accessing documentation strings
print(greet.__doc__)
# Output: This function greets the person passed in as a parameter.
