# for Statement
fruits = ['apple', 'banana', 'cherry', 'date']

for fruit in fruits:
    print(fruit, len(fruit))

# apple 5
# banana 6
# cherry 6
# date 4

# range() function
for number in range(1, 6):
    print(number)

# 1
# 2
# 3
# 4
# 5

# Range with different increment
print(list(range(5, 10)))
# [5, 6, 7, 8, 9]

print(list(range(0, 10, 3)))
# [0, 3, 6, 9]

print(list(range(-10, -100, -30)))
# [-10, -40, -70]

# Accessing elements and their indices
fruits = ['apple', 'banana', 'cherry', 'date']

for index in range(len(fruits)):
    print(f'Index {index}: {fruits[index]}')

# Index 0: apple
# Index 1: banana
# Index 2: cherry
# Index 3: date

for index, fruit in enumerate(fruits):
    print(f'Index {index}: {fruit}')

# Index 0: apple
# Index 1: banana
# Index 2: cherry
# Index 3: date
