# Creating a Set
unique_numbers = {1, 2, 3, 4, 5, 1, 2, 3}

# Printing the set
print('Set of Unique Numbers:', unique_numbers)  # Output: Set of Unique Numbers: {1, 2, 3, 4, 5}

# Set operations

# Creating two sets
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

# Intersection of sets
intersection_result = set_A.intersection(set_B)
print('Intersection result:', intersection_result)  # Output: Intersection result: {4, 5}

# Union of sets
union_result = set_A.union(set_B)
print('Union result:', union_result)  # Output: Union result: {1, 2, 3, 4, 5, 6, 7, 8}

# Difference of sets
difference_result = set_A.difference(set_B)
print('Difference result:', difference_result)  # Output: Difference result: {1, 2, 3}

# Adding and removing elements

# Creating a set
programming_languages = {'Python', 'JavaScript', 'Java'}

# Adding an element
programming_languages.add('C#')
print('Updated set with C#:', programming_languages)
# Output: Updated set with C#: {'C#', 'Java', 'Python', 'JavaScript'}

# Removing an element
programming_languages.remove('JavaScript')
print('Updated set without JavaScript:', programming_languages)
# Output: Updated set without JavaScript: {'C#', 'Java', 'Python'}

# Checking membership

# Creating a set
fruits_set = {'Apple', 'Banana', 'Cherry'}

# Checking membership
is_banana_present = 'Banana' in fruits_set
print('Is banana present?', is_banana_present)  # Output: Is banana present? True

is_orange_present = 'Orange' in fruits_set
print('Is orange present?', is_orange_present)  # Output: Is orange present? False

# Set comprehension

# Set comprehension to create a set of squares
squares_set = {x ** 2 for x in range(1, 6)}

# Printing the set of squares
print('Set of squares:', squares_set)  # Output: Set of squares: {1, 4, 9, 16, 25}















