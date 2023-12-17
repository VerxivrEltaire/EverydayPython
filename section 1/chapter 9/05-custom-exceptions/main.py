# Defining a simple custom exception
# class CustomError(Exception):
#     """A simple user-defined exception."""
#     pass
#
# # Raise the custom exception
# raise CustomError('This is a custom error message')

# Traceback (most recent call last):
#   File "/05-custom-exceptions/main.py", line 7, in <module>
#     raise CustomError('This is a custom error message')
# CustomError: This is a custom error message

# Adding additional information to the exception
# class DetailedError(Exception):
#     """A user-defined exception with additional information."""
#     def __init__(self, code, message):
#         self.code = code
#         self.message = message
#         super().__init__(f'Error {code}: {message}')
#
# # Raise the detailed custom exception
# raise DetailedError(404, 'Page not found')

# Traceback (most recent call last):
#   File "/05-custom-exceptions/main.py", line 23, in <module>
#     raise DetailedError(404, 'Page not found')
# DetailedError: Error 404: Page not found

# Handling user-defined exceptions
class InsufficientFundsError(Exception):
    """A custom exception for insufficient funds."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds. Balance: {balance}, Attempted amount: {amount}')

# Example of handling the custom exception
try:
    raise InsufficientFundsError(100, 150)
except InsufficientFundsError as ife:
    print(f'Error: {ife}')

# Output: Error: Insufficient funds. Balance: 100, Attempted amount: 150



