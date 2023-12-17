# Division by zero
result = 10 / 0

# Traceback (most recent call last):
#   File "/02-exceptions/main.py", line 2, in <module>
#     result = 10 / 0
#              ~~~^~~
# ZeroDivisionError: division by zero

# Index error
numbers = [1, 2, 3]
print(numbers[4])

# Traceback (most recent call last):
#   File "/02-exceptions/main.py", line 12, in <module>
#     print(numbers[4])
#           ~~~~~~~^^^
# IndexError: list index out of range

# Type error
result = '10' + 5

# Traceback (most recent call last):
#   File "/02-exceptions/main.py", line 21, in <module>
#     result = '10' + 5
#              ~~~~~^~~
# TypeError: can only concatenate str (not "int") to str

# try and except
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f'Error: {e}')
    result = 'undefined'

# Output: Error: division by zero

# Multiple exceptions
try:
    value = int('ten')
except (RuntimeError, ValueError, TypeError) as e:
    print(f'Error: {e}')
    value = 0

# Output: Error: invalid literal for int() with base 10: 'ten'

# else and finally
try:
    file = open('existing_file.txt', 'r')
except FileNotFoundError:
    print('File not found.')
else:
    content = file.read()
    print(content)
finally:
    file.close()








