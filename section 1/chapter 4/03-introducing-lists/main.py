# Creating a list
number_list = [1, 2, 3, 4, 5]
fruit_list = ['apple', 'banana', 'cherry', 'date', 'fig']
mixed_list = [42, 'hello', 3.14, True]

# Accessing list elements
first_fruit = fruit_list[0]  # 'apple'
second_fruit = fruit_list[1]  # 'banana'
last_fruit = fruit_list[-1]  # 'fig'

# Slicing with steps
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = numbers[0::2]  # [0, 2, 4, 6, 8]

# Negative indexing and slicing
last_fruit = fruit_list[-1]  # 'fig'
last_three = fruit_list[-3:]  # ['cherry', 'date', 'fig']

# Modifying lists

# Update an element
number_list[2] = 99  # [1, 2, 99, 4, 5]

# Extend the list using the append method
number_list.append(6)  # [1, 2, 99, 4, 5, 6]

# Modifying slices
number_list[1:4] = ['A', 'B', 'C']  # [1, 'A', 'B', 'C', 5, 6]
number_list[:] = []  # []. clear the list by replacing all the elements with an empty list

# List operations
fruits1 = ['apple', 'banana']
fruits2 = ['cherry', 'date']

combined_fruits = fruits1 + fruits2  # ['apple', 'banana', 'cherry', 'date']
repeated_fruits = fruits1 * 3  # ['apple', 'banana', 'apple', 'banana', 'apple', 'banana']

# len() function
len(repeated_fruits)  # 6

# Nested lists
d = ['a', 'b', 'c']
e = [1, 2, 3]
f = [d, e]

print(f)  # [['a', 'b', 'c'], [1, 2, 3]]
print(f[0])  # ['a', 'b', 'c']
print(f[0][1])  # b
