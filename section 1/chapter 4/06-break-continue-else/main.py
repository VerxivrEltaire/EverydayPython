# The break Statement
fruits = ['apple', 'banana', 'cherry', 'date']
search_fruit = 'cherry'

for fruit in fruits:
    if fruit == search_fruit:
        print(f'{search_fruit} found!')
        break
else:
    print(f'{search_fruit} not found.')

# The continue Statement
fruits = ['apple', 'banana', 'cherry', 'date']

for fruit in fruits:
    if fruit == 'banana':
        continue
    print(fruit)

# apple
# cherry
# date

for num in range(2, 10):
    if num % 2 == 0:
        print("An even number found", num)
        continue
    print("An odd number found", num)

# An even number found 2
# An odd number found 3
# An even number found 4
# An odd number found 5
# An even number found 6
# An odd number found 7
# An even number found 8
# An odd number found 9

# The else Statement
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3
