# Basic lambda expression
add = lambda e, f: e + f

result = add(3, 5)
print(result)  # Output: 8


# Lambda functions as arguments
numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers, key=lambda x: x % 3)

print(sorted_numbers)  # Output: [9, 1, 5, 2, 8]

# Lambda functions as arguments
pairs = [(1, 'fire'), (2, 'water'), (3, 'wind'), (4, 'air')]
pairs.sort(key=lambda pair: pair[1])

print(pairs)  # Output: [(4, 'air'), (1, 'fire'), (2, 'water'), (3, 'wind')]

# Lambda functions for mapping
numrs = [6, 4, 2, 5, 3]
squared_numrs = list(map(lambda x: x ** 2, numrs))

print(squared_numrs)  # Output: [36, 16, 4, 25, 9]

# Lambda functions for filtering
numrs = [6, 4, 2, 5, 3]
even_numbers = list(filter(lambda x: x % 2 == 0, numrs))

print(even_numbers)  # Output: [6, 4, 2]

