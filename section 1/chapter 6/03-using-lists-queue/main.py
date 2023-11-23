# Creating a deque
from collections import deque

# Creating a deque
my_deque = deque(['Apple', 'Banana', 'Cherry'])

# Appending to the right
my_deque.append('Date')

# Appending to the left
my_deque.appendleft('Avocado')

print(my_deque)  # Output: deque(['Avocado', 'Apple', 'Banana', 'Cherry', 'Date'])

# Popping from both ends

# Popping from the right
popped_right = my_deque.pop()

# Popping from the left
popped_left = my_deque.popleft()

print('Popped Right:', popped_right)  # Output: Popped Right: Date
print('Popped Left:', popped_left)  # Output: Popped Left: Avocado
print(my_deque)  # Output: deque(['Apple', 'Banana', 'Cherry'])

# Rotating the deque

# Rotating to the right
my_deque.rotate(1)

# Rotating to the left
my_deque.rotate(-1)

print(my_deque)  # Output: deque(['Banana', 'Cherry', 'Apple'])

# Maximizing performance
import timeit

# Using lists for comparison
list_time = timeit.timeit('lst.pop(0)', setup='lst = list(range(10000))', number=1000)
deque_time = timeit.timeit('dq.popleft()', setup='from collections import deque; dq = deque(range(10000))', number=1000)

print('List Time:', list_time)
print('Deque Time:', deque_time)
