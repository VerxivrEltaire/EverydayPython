# Positional arguments
def add(a, b):
    return a + b


result = add(3, 5)
print(result)  # Output: 8


# Variable length positional arguments
def calculate_sum(*args):
    return sum(args)


result1 = calculate_sum(1, 2, 3)
result2 = calculate_sum(10, 20, 30, 40)

print(result1)  # Output: 6
print(result2)  # Output: 100

def nursery_rhyme(*args):
    for arg in args:
        print(arg, end=' ')

nursery_rhyme('Mary had', 'a little lamb')
# Output: Mary had a little lamb

# Keyword arguments
def calculate_area(length, width):
    return length * width


area1 = calculate_area(4, 5)  # using positional arguments
area2 = calculate_area(length=4, width=5)  # using keyword arguments
area3 = calculate_area(width=5, length=4)  # using keyword arguments in a different order

print(area1)  # Output: 20
print(area2)  # Output: 20
print(area3)  # Output: 20

# Variable length keyword arguments
def describe_person(**kwargs):
    description = f"{kwargs['name']} is {kwargs['age']} years old."
    if 'city' in kwargs:
        description += f" Lives in {kwargs['city']}."
    return description

result1 = describe_person(name='Alice', age=30)
result2 = describe_person(name='Bob', age=25, city='New York')

print(result1)  # Output: 'Alice is 30 years old.'
print(result2)  # Output: 'Bob is 25 years old. Lives in New York.'


def user_status(**kwargs):
    for kw in kwargs:
        print(kw, ':', kwargs[kw])

user_status(John='Active', Ada='Inactive', Chioma='Active')

# John : Active
# Ada : Inactive
# Chioma : Active