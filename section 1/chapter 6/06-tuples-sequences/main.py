# Understanding Tuples

# Creating a tuple
fruits_tuple = ('Apple', 'Banana', 'Cherry')

# Accessing elements in a tuple
first_fruit = fruits_tuple[0]
print('First fruit:', first_fruit)  # Output: First fruit: Apple

# Attempting to modify a tuple (will raise an error)
# fruits_tuple[0] = 'Apricot'  # Uncommenting this line will result in an error

# Versatility of tuples

# Creating a mixed-type tuple
person_info = ('Alice', 30, True, 'Developer')

# Accessing elements in a mixed-type tuple
name = person_info[0]
age = person_info[1]

print('Name:', name)  # Output: Name: Alice
print('Age:', age)  # Output: Age: 30

# Tuple unpacking

# Creating a tuple
coordinates = (3, 7)

# Unpacking the tuple
x, y = coordinates

print('X Coordinate:', x)  # Output: X Coordinate: 3
print('Y Coordinate:', y)  # Output: Y Coordinate: 7

# Creating nested tuples

# Creating a nested tuple
person_data = ('Alice', (30, 'Developer'), ['Python', 'JavaScript'])

# Accessing elements in a nested tuple
job_title = person_data[1][1]
favorite_language = person_data[2][0]

print('Job title:', job_title)  # Output: Job title: Developer
print('Favorite language:', favorite_language)  # Output: Favorite language: Python

# Tuple methods and functions

# Creating a tuple
numbers = (3, 1, 4, 1, 5, 9)

# Finding the index of an element
index_of_5 = numbers.index(5)
print('Index of 5:', index_of_5)  # Output: Index of 5: 4

# Counting occurrences of an element
count_of_1 = numbers.count(1)
print('Count of 1:', count_of_1)  # Output: Count of 1: 2








