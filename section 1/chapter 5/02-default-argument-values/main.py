# Default argument values
def greet(name, greeting='Hello'):
    return f'{greeting}, {name}!'


# Calling the function
result1 = greet('Alice')  # Uses the default greeting
result2 = greet('Bob', 'Hi')  # Uses the provided greeting

print(result1)  # Output: 'Hello, Alice!'
print(result2)  # Output: 'Hi, Bob!'


# Function that calculates the area
def calculate_area(shape, width, height=None):
    if shape == 'rectangle':
        return width * height if height else 0
    elif shape == 'square':
        return width * width
    else:
        return 0


# Calculating areas
area1 = calculate_area('rectangle', 4, 5)  # Provides both width and height
area2 = calculate_area('square', 3)  # Provides only width
area3 = calculate_area('circle', 7)  # Unknown shape

print(area1)  # Output: 20
print(area2)  # Output: 9
print(area3)  # Output: 0

# Giving a response
def give_response(value='yes'):
    if value in ('y', 'ye', 'yes'):
        return 'Ok, you can try again'
    elif value in ('n', 'no', 'nop', 'nope'):
        return 'Sorry, you cannot try again'
    else:
        return 'Invalid user response'


response1 = give_response()  # uses the default value
response2 = give_response('no')  # provides a value

print(response1)  # Output: Ok, you can try again
print(response2)  # Output: Sorry, you cannot try again
