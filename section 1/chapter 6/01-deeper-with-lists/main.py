# The append method
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]

# The extend method
first_list = [10, 20]
second_list = [30, 40]
first_list.extend(second_list)
print(first_list)  # Output: [10, 20, 30, 40]

# The insert method
grades = ['A', 'C', 'D']
grades.insert(1, 'B')
print(grades)  # Output: ['A', 'B', 'C', 'D']

# The remove method
scores = [90, 85, 92, 88]
scores.remove(92)
print(scores)  # Output: [90, 85, 88]

# The pop method with an index
stack = [3, 5, 7]
popped_value = stack.pop(1)
print(popped_value)  # Output: 5

# The pop method without an index
stack = [3, 5, 7]
popped_value = stack.pop()
print(popped_value)  # Output: 7

# The clear method
data = ['Alpha', 'Beta']
data.clear()
print(data)  # Output: []

# The index method
numbers = [20, 10, 30, 10, 40]
position = numbers.index(10)
print(position)  # Output: 1

# The index method with start and stop values
numbers = [20, 10, 30, 10, 40]
position = numbers.index(10, 2, 4)
print(position)  # Output: 3

# The count method
tally_list = [5, 2, 5, 8, 5]
count_of_5 = tally_list.count(5)
print(count_of_5)  # Output: 3

# The sort method
random_order = [40, 10, 30, 20]
random_order.sort()
print(random_order)  # Output: [10, 20, 30, 40]

# The reverse method
original_order = ['First', 'Second', 'Third']
original_order.reverse()
print(original_order)  # Output: ['Third', 'Second', 'First']

# The copy method
original_list = ['Item1', 'Item2', 'Item3']
replicated_list = original_list.copy()
print(replicated_list)  # Output: ['Item1', 'Item2', 'Item3']
