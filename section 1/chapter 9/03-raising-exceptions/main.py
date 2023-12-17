# Custom exception
def validate_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative.')

try:
    validate_age(-5)
except ValueError as e:
    print(f'Error: {e}')

# Output: Error: Age cannot be negative.


