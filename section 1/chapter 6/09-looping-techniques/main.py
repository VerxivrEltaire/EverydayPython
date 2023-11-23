# Looping through Dictionaries
import math

# Creating a dictionary of person information
person_info = {'name': 'Alice', 'age': 30, 'occupation': 'Developer'}

for k, v in person_info.items():
    print(f'{k}: {v}')

# Output
# name: Alice
# age: 30
# occupation: Developer

# Looping through Sequences
for i, v in enumerate(['bicycle', 'car', 'plane']):
    print(f'{i}: {v}')

# Output
# 0: bicycle
# 1: car
# 2: plane

# Looping through two or more Sequences
questions = ['name', 'age', 'marital status']
answers = ['Mary', 'Thirty', 'Single']

for q, a in zip(questions, answers):
    print(f'What is your {q}?  It is {a}.')

# Output
# What is your name?  It is Mary.
# What is your age?  It is Thirty.
# What is your marital status?  It is Single.

# Looping through Sequences in reverse
for i in reversed(range(1, 12, 2)):
    print(i)

# Output
# 11
# 9
# 7
# 5
# 3
# 1

# Looping through Sequences in sorted order
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# Output
# apple
# apple
# banana
# orange
# orange
# pear

# Looping through unique elements in Sequences in sorted order
for f in sorted(set(basket)):
    print(f)

# Output
# apple
# banana
# orange
# pear

# Creating a new list when looping
data = [26.5, float('NaN'), 31.6, 65.4, float('NaN'), 12.9, float('NaN'), 87.2]

filtered_data = []
for value in data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)  # Output: [26.5, 31.6, 65.4, 12.9, 87.2]
