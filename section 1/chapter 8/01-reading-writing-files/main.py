# The open() function

# Opening a file in read mode
file_path = 'sample.txt'
with open(file_path, 'r', encoding="utf-8") as file:
    # File operations go here
    content = file.read()
    print(content)

# File automatically closed outside the 'with' block

