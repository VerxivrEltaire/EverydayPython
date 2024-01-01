# Creating a simple list

# Using a loop to create a list of squares
squares_with_loop = []
for num in range(5):
    squares_with_loop.append(num ** 2)

# Using lambdas
squares_with_lambdas = list(map(lambda num: num ** 2, range(5)))

# Using list comprehension for the same task
squares_with_comprehension = [num ** 2 for num in range(5)]

print('Squares with loop:', squares_with_loop)
print('Squares with lambdas:', squares_with_lambdas)
print('Squares with Comprehension:', squares_with_comprehension)

# Output: Squares with loop: [0, 1, 4, 9, 16]
# Output: Squares with lambdas: [0, 1, 4, 9, 16]
# Output: Squares with comprehension: [0, 1, 4, 9, 16]

# Combining two lists with comprehension
combined_with_comp = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

# This is equivalent to
combined_with_loop = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combined_with_loop.append((x, y))

print('Combined with comprehension:', combined_with_comp)
print('Combined with loop:', combined_with_loop)

# Output: Combined with comp: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
# Output: Combined with loop: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# Performing comprehensions
base_list = [2, 3, -1, 0, 3, 5]

# create a new list with the values doubled
doubled_list = [num * 2 for num in base_list]
print(doubled_list)  # Output: [4, 6, -2, 0, 6, 10]

# filter the list to exclude negative numbers
filtered_list = [num for num in base_list if num >= 0]
print(filtered_list)  # Output: [2, 3, 0, 3, 5]

# apply a function to all the elements
applied_list = [abs(num) for num in base_list]
print(applied_list)  # Output: [2, 3, 1, 0, 3, 5]

fruit_list = [' banana ', ' apple ', ' lemon ', ' grape ']

# call a method on each element
method_call_list = [fruit.strip() for fruit in fruit_list]
print(method_call_list)  # Output: ['banana', 'apple', 'lemon', 'grape']

# create a list of 2-tuples like (number, square)
tuple_list = [(num, num ** 2) for num in range(5)]
print(tuple_list)  # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

# flatten a list using a list comprehension with two 'for' loops
value_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [num for element in value_list for num in element]
print(new_list)  # Output: # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Filtering with list comprehension

# Using a loop to filter even numbers
evens_with_loop = []
for num in range(10):
    if num % 2 == 0:
        evens_with_loop.append(num)

# Using list comprehension for the same filtering
evens_with_comprehension = [num for num in range(10) if num % 2 == 0]

print('Evens with loop:', evens_with_loop)
print('Evens with comprehension:', evens_with_comprehension)

# Output: Evens with loop: [0, 2, 4, 6, 8]
# Output: Evens with comprehension: [0, 2, 4, 6, 8]

# Creating a matrix

# Using nested loops to create a matrix
matrix_with_loop = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i * j)
    matrix_with_loop.append(row)

# Using nested list comprehension for the same matrix
matrix_with_comprehension = [[i * j for j in range(3)] for i in range(3)]

print('Matrix with loop:', matrix_with_loop)
print('Matrix with comprehension:', matrix_with_comprehension)

# Output: Matrix with loop:
# [
#   [0, 0, 0],
#   [0, 1, 2],
#   [0, 2, 4]
# ]

# Output: Matrix with comprehension:
# [
#   [0, 0, 0],
#   [0, 1, 2],
#   [0, 2, 4]
# ]

# Transposing rows and columns in a matrix with nested list comprehension
matrix_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# Using loops to transpose the matrix
transposed_list = []
for i in range(4):
    transposed_list.append([row[i] for row in matrix_list])

# or
transposed_list = []
for i in range(4):
    # the following 3 lines implement the nested list comprehension
    transposed_row = []
    for row in matrix_list:
        transposed_row.append(row[i])
    transposed_list.append(transposed_row)

# Using list comprehension to transpose the matrix
transposed_list = [[row[i] for row in matrix_list] for i in range(4)]

print('Transposed matrix with loop:', transposed_list)
print('Transposed matrix with comprehension:', transposed_list)

# Output: Transposed matrix with loop:
# [
#   [1, 5, 9],
#   [2, 6, 10],
#   [3, 7, 11],
#   [4, 8, 12]
# ]

# Output: Transposed matrix with comprehension:
# [
#   [1, 5, 9],
#   [2, 6, 10],
#   [3, 7, 11],
#   [4, 8, 12]
# ]

# The zip function
zip_list = list(zip(*matrix_list))
print('Transposed matrix with zip function:', zip_list)

# Output: Transposed matrix with zip function:
# [
#   [1, 5, 9],
#   [2, 6, 10],
#   [3, 7, 11],
#   [4, 8, 12]
# ]

# List comprehension with conditionals

# Using a loop to filter and square odd numbers
squares_of_odds_with_loop = []
for num in range(7):
    if num % 2 != 0:
        squares_of_odds_with_loop.append(num ** 2)

# Using list comprehension for the same task
squares_of_odds_with_comprehension = [num ** 2 for num in range(7) if num % 2 != 0]

print('Squares of odds with loop:', squares_of_odds_with_loop)
print('Squares of odds with comprehension:', squares_of_odds_with_comprehension)

# Output: Squares of odds with loop: [1, 9, 25]
# Output: Squares of odds with comprehension: [1, 9, 25]



