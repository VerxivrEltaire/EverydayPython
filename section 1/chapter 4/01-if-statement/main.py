# Basic if statement
age = 18

if age >= 18:
    print('You are an adult.')
# You are an adult.

# if and else
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# elif
grade = 75

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")
# C

# Nested if statement
age = 18
income = 30000

if age >= 18:
    if income >= 30000:
        print("You are eligible for a loan.")
    else:
        print("You are not eligible for a loan.")
else:
    print("You are not eligible for a loan.")

# and Operator
x = 5
y = 10

if x < 10 and y > 5:
    print('Both conditions are true')
else:
    print('At least one condition is false')
# Both conditions are true

# or Operator
x = 5
y = 3

if x < 10 or y > 5:
    print('At least one condition is true')
else:
    print('Both conditions are false')

# At least one condition is true

# not Operator
x = 5

if not x > 10:
    print('x is not greater than 10')
else:
    print('x is greater than 10')

# x is not greater than 10

# Combining Logical Operators
x = 5
y = 12

if (x > 0 and y < 10) or (x < 10 and y > 0):
    print('Complex condition is true')
else:
    print('Complex condition is false')

# Complex condition is true



