# Basic exception chaining
try:
    # Some code that may raise an exception
    num = int('abc')
except ValueError as ve:
    # Handling the exception and raising a new one
    raise RuntimeError('Custom error occurred') from ve

# Traceback (most recent call last):
#   File "04-exception-chaining/main.py", line 4, in <module>
#     num = int('abc')
#           ^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'abc'
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
#   File "/04-exception-chaining/main.py", line 7, in <module>
#     raise RuntimeError('Custom error occurred') from ve
# RuntimeError: Custom error occurred

# Multiple exception chaining
try:
    # Some code that may raise different exceptions
    result = 10 / 0
except ZeroDivisionError as zd_err:
    # Handling a specific exception and chaining another
    raise ValueError('Invalid calculation') from zd_err
except Exception as e:
    # Handling other exceptions
    raise RuntimeError('Unexpected error') from e

# Traceback (most recent call last):
#   File "/04-exception-chaining/main.py", line 25, in <module>
#     result = 10 / 0
#              ~~~^~~
# ZeroDivisionError: division by zero
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
#   File "/04-exception-chaining/main.py", line 28, in <module>
#     raise ValueError('Invalid calculation') from zd_err
# ValueError: Invalid calculation

# Nested exception chaining
try:
    try:
        # Some code that may raise an exception
        value = int('abc')
    except ValueError as inner_err:
        # Handling the inner exception and raising a new one
        raise RuntimeError('Inner error occurred') from inner_err
except RuntimeError as outer_err:
    # Handling the outer exception
    print(f'Outer exception: {outer_err.__cause__}')

# Output: Outer exception: invalid literal for int() with base 10: 'abc'