# Basic match syntax
match value:
    case pattern1:
        # Code to execute if pattern1 matches
    case pattern2:
        # Code to execute if pattern2 matches
    case patternN:
        # Code to execute if patternN matches
    case _:
        # Default code to execute if no patterns match

# Patterns and matching
match day:
    case 1:
        print("It's Monday!")
    case 7:
        print("It's Sunday!")
    case _:
        print("It's another day of the week.")

# Sequences and destructuring
match coordinates:
    case (0, 0):
        print("You're at the origin.")
    case (x, 0):
        print(f"You're on the x-axis at {x}.")
    case (0, y):
        print(f"You're on the y-axis at {y}.")
    case (x, y):
        print(f"You're at ({x}, {y}).")

# Enums and custom classes
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

match user_color:
    case Color.RED:
        print("You chose red.")
    case Color.GREEN:
        print("You chose green.")
    case Color.BLUE:
        print("You chose blue.")
    case _:
        print("You chose an unknown color.")


