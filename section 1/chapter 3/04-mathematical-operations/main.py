# Addition, subtraction, multiplication and division
a = 10
b = 5

addition_result = a + b
print(addition_result)  # 15

subtraction_result = a - b
print(subtraction_result)  # 5

multiplication_result = a * b
print(multiplication_result)  # 50

division_result = a / b
print(division_result)  # 2.0 (even if both a and b are integers, division results in a float)

# Integer (floor) division
integer_division_result = a // b
print(integer_division_result)  # 2

# Round to 2 decimal places
round_result = round(8 / 3, 4)
print(round_result)

# Modulo (Remainder)
remainder = a % b
print(remainder)  # 0 (since 10 divided by 5 leaves no remainder)

# Exponentiation
c = 2
exponent_result = c ** 3
print(exponent_result)  # 8 (2 raised to the power of 3)

# Math functions
import math

square_root = math.sqrt(25)
print(square_root)  # 5.0 (square root)

absolute_value = math.fabs(-3)
print(absolute_value)  # 3.0 (absolute value)

# Order of Operations
print(5 * (4 + 3) / 2 - 6)
# 11.5

# Complex mathematical operations
result = (a + b) * (c ** 2) + math.sqrt(16)
print(result)
# 64

