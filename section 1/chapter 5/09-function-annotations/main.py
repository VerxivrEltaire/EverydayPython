# Basic function annotation
def add(w: int, v: int) -> int:
    return w + v

# Function annotations for clarity
def cal_area(lth: float, wth: float) -> float:
    return lth * wth

# Complex function annotations
from typing import List

def find_largest(numbers: List[int]) -> int:
    return max(numbers)
