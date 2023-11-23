# Defining a function
def greet(name):
    print(f'Hello, {name}!')


# Calling the function
greet('Alice')  # Output: 'Hello, Alice!'


# A function accepting arguments
def add(x, y):
    result = x + y
    print(result)


add(3, 5)


# Returning results
def multiply(x, y):
    result = x * y
    return result


product = multiply(4, 6)
print(product)  # Output: 24


# Returning Fibonacci series up to n
def fibonacci(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1

    while a < n:
        result.append(a)  # see below
        a, b = b, a + b
    return result


fibonacci100 = fibonacci(100)
print(fibonacci100)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Function local symbol table
global_variable = 42  # Global variable


def my_function():
    local_variable = 10  # Local variable
    print(f"Local variable: {local_variable}")
    print(f"Accessing global variable from the function: {global_variable}")


my_function()


# print(f"Accessing local variable from the global scope: {local_variable}")  # This will result in an error

# Call by Object reference
def modify_list(my_list):
    my_list.append(4)  # changes made here affect original object
    my_list = [1, 2, 3]  # new local list variable. Does not affect original object


original_list = [0]
modify_list(original_list)

print(original_list)  # Output: [0, 4]

