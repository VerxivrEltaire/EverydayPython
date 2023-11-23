# Argument unpacking
def add(a, b):
    return a + b

values = (3, 5)  # a tuple

result = add(*values)
print(result)  # Output: 8

# Mixing unpacked arguments with positional arguments
def multiply(a, b, c):
    return a * b * c

values = [2, 3]
result = multiply(4, *values)

print(result)  # Output: 24

# Unpacking in functions
def average(*args):
    return sum(args) / len(args)

result = average(1, 2, 3, 4, 5)

print(result)  # Output: 3.0

# Unpacking dictionary values
def describe_person(name, age, city):
    return f"{name} is {age} years old and lives in {city}."

info = {'name': 'Alice', 'age': 30, 'city': 'New York'}
result = describe_person(**info)

print(result)  # Output: 'Alice is 30 years old and lives in New York.'
