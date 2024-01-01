# Creating and manipulating a stack
stack = []  # creating an empty stack

# Appending elements onto the stack
stack.append('Apple')
stack.append('Banana')
stack.append('Cherry')

print(stack)  # Output: ['Apple', 'Banana', 'Cherry']

# Popping an element from the stack
popped_item = stack.pop()
print('Popped:', popped_item)  # Output: Popped: Cherry
print(stack)  # Output: ['Apple', 'Banana']

# Peeking into the stack
stack = ['Orange', 'Grapes', 'Mango']

# Peeking at the top element
top_element = stack[-1]
print('Top element:', top_element)  # Output: Top element: Mango
print(stack)  # Output: ['Orange', 'Grapes', 'Mango']

# Checking if the stack is empty
stack = []

if not stack:
    print('The stack is empty.')
else:
    print('The stack is not empty.')
