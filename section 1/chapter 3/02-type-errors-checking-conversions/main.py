# Type errors
x = "5"
y = 3
result = x + y

# Traceback (most recent call last):
#   File "/Everyday Python/section 1/chapter 3/02-type-errors-checking-conversions/main.py", line 4, in <module>
#     result = x + y
#              ~~^~~
# TypeError: can only concatenate str (not "int") to str

# Type checking
x = 5
y = "Hello"

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>

# Converting to an integer
x = "5"
y = int(x)  # Convert string to integer

# Converting to a float
x = "3.14"
y = float(x)  # Convert string to float

# Converting to a string
x = 42
y = str(x)  # Convert integer to string

# Handling type errors
user_input = input("Enter a number: ")

if user_input.isnumeric():
    num = int(user_input)
    result = num * 2
    print(f"Double the number: {result}")
else:
    print("Invalid input. Please enter a numeric value.")

