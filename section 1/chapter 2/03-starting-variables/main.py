name = 'James Bond'

width = 20
width = 30
print(width)
# 30

integer_var = 42
float_var = 3.14
string_var = "Hello, World!"
list_var = [1, 2, 3, 4, 5]
dict_var = {'name': 'Chioma', 'age': 45}

# Type checking variables
print(type(integer_var))  # <class 'int'>
print(type(float_var))  # <class 'float'>
print(type(string_var))  # <class 'str'>

# Variable scope
global_var = 100


def my_function():
    local_var = 42  # Local variable
    print(global_var)  # Accessing the global variable


my_function()
# print(local_var)  # This will result in an error since local_var is not accessible here.

# Naming convention
first_name = "Timi"
last_name = "Ojukwu"

# Dynamic typing
x = 5
x = "Hello"  # x is now a string

print(x)
# Hello

# [Interactive coding exercise] Variables
a = input()
b = input()

c = a
a = b
b = c

print('a: ' + a)
print('b: ' + b)
print(a + ' ' + b)










