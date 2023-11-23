# Understanding Dictionaries

# Creating a dictionary of person information
person_info = {'name': 'Alice', 'age': 30, 'occupation': 'Developer'}

# Accessing values using keys
name = person_info['name']
age = person_info['age']

print('Name:', name)  # Output: Name: Alice
print('Age:', age)  # Output: Age: 30

# Dynamic nature of Dictionaries

# Adding a new key-value pair
person_info['location'] = 'Wonderland'
print('Updated person info:', person_info)
# Output: Updated person info: {'name': 'Alice', 'age': 30, 'occupation': 'Developer', 'location': 'Wonderland'}

# Modifying an existing value
person_info['age'] = 31
print('Modified person info:', person_info)
# Output: Modified person info: {'name': 'Alice', 'age': 31, 'occupation': 'Developer', 'location': 'Wonderland'}

# Removing a key-value pair
removed_occupation = person_info.pop('occupation')

print('Removed occupation:', removed_occupation)  # Output: Removed occupation: Developer

print('Final person info:', person_info)
# Output: Final person info: {'name': 'Alice', 'age': 31, 'location': 'Wonderland'}

# Dictionary methods and functions

# Creating a dictionary of grades
grades = {'Alice': 90, 'Bob': 85, 'Charlie': 92}

# Checking if a key exists
is_bob_present = 'Bob' in grades
print('Is Bob present?', is_bob_present)  # Output: Is Bob present? True

# Getting a list of keys and values
all_names = grades.keys()
all_scores = grades.values()

print('All names:', all_names)  # Output: All names: dict_keys(['Alice', 'Bob', 'Charlie'])
print('All scores:', all_scores)  # Output: All scores: dict_values([90, 85, 92])

# Nested Dictionaries

# Creating a nested dictionary
employees = {
    'Alice': {'position': 'Manager', 'experience': 5},
    'Bob': {'position': 'Developer', 'experience': 3}
}

# Accessing values in a nested dictionary
bob_position = employees['Bob']['position']
print('Bob\'s Position:', bob_position)  # Output: Bob's Position: Developer

# Dictionary comprehension

# Dictionary comprehension to create a dictionary of squares
squares_dict = {x: x**2 for x in range(1, 6)}

# Printing the dictionary of squares
print('Dictionary of squares:', squares_dict)
# Output: Dictionary of squares: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Building Dictionaries
info_dict = dict([('name', 'Ade'), ('age', 'Thirty'), ('status', 'Married')])
print(info_dict)  # Output: {'name': 'Ade', 'age': 'Thirty', 'status': 'Married'}

info_dict = dict(name='Ade', age='Thirty', status='Married')
print(info_dict)  # Output: {'name': 'Ade', 'age': 'Thirty', 'status': 'Married'}
