# Math module
import math

radius = 5
area = math.pi * math.pow(radius, 2)
print(f'The area of a circle with radius {radius} is: {area}')

# Output: The area of a circle with radius 5 is: 78.53981633974483

# Datetime module
from datetime import datetime, timedelta

current_time = datetime.now()
future_time = current_time + timedelta(days=7)
print(f'Current time: {current_time}\nFuture time: {future_time}')

# Output:
# Current time: 2023-11-25 19:38:33.315743
# Future time: 2023-12-02 19:38:33.315743

# Random module
import random

dice_roll = random.randint(1, 6)
print(f'The dice rolled: {dice_roll}')

# Output: The dice rolled: 1

# Sys module
import sys

print(f'Python version: {sys.version}\nPlatform: {sys.platform}')

# Output:
# Python version: 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)]
# Platform: darwin

# OS module
import os

current_directory = os.getcwd()
print(f'Current directory: {current_directory}')

# Output:
# Current directory: /Everyday Python/section 1/chapter 7/02-modules-as-scripts

# Collections module
from collections import Counter

fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
fruit_count = Counter(fruits)
print(f'Fruit count: {fruit_count}')

# Output: Fruit count: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# JSON module
import json

data = '{"name": "John", "age": 30, "city": "New York"}'
parsed_data = json.loads(data)
print(f"Name: {parsed_data['name']}, Age: {parsed_data['age']}")

# Output: Name: John, Age: 30
