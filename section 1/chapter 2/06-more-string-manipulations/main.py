name = 'Jide'
age = 35

print('Hi ' + name + ' you are ' + str(age) + ' years old')
# Concatenating and type conversion to successfully print

# Hi Jide you are 35 years old

print(f'Hi {name} you are {age} years old')
# Notice the 'f' and the curly braces around the variables

# Hi Jide you are 35 years old

# Indexing
country = 'Nigeria'

print(country[0])  # character in position 0
# N

print(country[5])  # character in position 5
# i

print(country[-1])  # last character
# a

print(country[-2])  # second-last character
# i

print(country[-5])
# g

# print(country[52])
# Traceback (most recent call last):
#   File "Everyday Python/section 1/chapter 2/04-more-string-manipulations/main.py", line 32, in <module>
#     print(country[52])
#           ~~~~~~~^^^^
# IndexError: string index out of range

# Slicing
print(country[0:5])  # characters from position 0 (included) to 5 (excluded)
# Niger

print(country[2:6])  # characters from position 2 (included) to 6 (excluded)
# geri

print(country[:4])  # characters from the beginning to position 4 (excluded)
# Nige

print(country[4:])  # characters from position 4 (included) to the end
# ria

print(country[-4:])  # characters from fourth-last 4 (included) to the end
# eria

print(country[4:52])
# ria

print(country[43:])
# ''

print(len(country))
# 7

country[4] = 'j'

# Traceback (most recent call last):
#   File "/Everyday Python/section 1/chapter 2/04-more-string-manipulations/main.py", line 61, in <module>
#     country[4] = 'j'
#     ~~~~~~~^^^
# TypeError: 'str' object does not support item assignment
