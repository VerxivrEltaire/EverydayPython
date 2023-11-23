# Basic lambda expression
add = lambda x, y: x + y

result = add(3, 5)
print(result)  # Output: 8

# Lambda functions as arguments
numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers, key=lambda x: x % 3)

print(sorted_numbers)  # Output: [9, 1, 5, 2, 8]

# Lambda functions as arguments
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])

print(pairs)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# Lambda functions for mapping
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Lambda functions for filtering
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4]
