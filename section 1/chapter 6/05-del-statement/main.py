# Deleting variables

# Creating a variable
user_name = 'Alice'
print('Original Name:', user_name)

# Using del to delete the variable
del user_name

# Attempting to print the variable after deletion (will raise an error)
# print('Deleted Name:', user_name)  # Uncommenting this line will result in an error

# Deleting elements from a list

# Creating a list
fruits = ['Apple', 'Banana', 'Cherry', 'Date']
print('Original list:', fruits)
# Output: Original list: ['Apple', 'Banana', 'Cherry', 'Date']

# Using del to remove the second element
del fruits[1]
print('List after deletion:', fruits)
# Output: List after deletion: ['Apple', 'Cherry', 'Date']

# Deleting slices

# Creating a list
numbers = [1, 2, 3, 4, 5]
print('Original list:', numbers)

# Output: Original list: [1, 2, 3, 4, 5]

# Using del to remove a slice
del numbers[1:4]
print('List after slice deletion:', numbers)

# Output: List after slice deletion: [1, 5]

# Deleting attributes from Objects

# Creating a simple class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object
alice = Person('Alice', 30)
print('Original age:', alice.age) # Output: Original age: 30

# Using del to delete an attribute
del alice.age
# Attempting to access the deleted attribute (will raise an error)
# print('Deleted age:', alice.age)  # Uncommenting this line will result in an error

