# Basic function annotation
def add(x: int, y: int) -> int:
    return x + y

# Function annotations for clarity
def calculate_area(length: float, width: float) -> float:
    return length * width

# Complex function annotations
from typing import List

def find_largest(numbers: List[int]) -> int:
    return max(numbers)
