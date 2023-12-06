# JSON serialization
import json

# A Python dictionary
book = {
    'title': 'Python Unleashed',
    'author': 'Code Maestro',
    'price': 29.99
}

# Serialize the dictionary to a JSON string
json_string = json.dumps(book)

print(json_string)

# JSON deserialization

# Deserialize the JSON string back to a Python dictionary
decoded_book = json.loads(json_string)
print(decoded_book)

# JSON to files

# Save the JSON string to a file
with open('book.json', 'w') as file:
    json.dump(book, file)

# Read the JSON string from the file
with open('book.json', 'r') as file:
    loaded_book = json.load(file)

print(loaded_book)
