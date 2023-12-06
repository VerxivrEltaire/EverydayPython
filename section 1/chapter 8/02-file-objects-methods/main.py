# The read() method
file_path = 'sample.txt'
with open(file_path, 'r') as file:
    content = file.read(20)  # Read the first 20 characters
    print(content)

# The readline() method
with open(file_path, 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1.strip())
    print(line2.strip())

# The readlines() method
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines[:3]:  # Displaying the first three lines
        print(line.strip())

# The write() method
with open(file_path, 'a') as file:
    file.write("\nA new section begins.")

# The writelines() method
new_lines = ["The adventure unfolds.", "In the realm of Python."]
with open(file_path, 'a') as file:
    file.writelines('\n' + line for line in new_lines)

# The seek() method
with open(file_path, 'r') as file:
    file.seek(10)  # Move to the 10th byte
    content = file.read(15)
    print(content)

# The tell() method
with open(file_path, 'r') as file:
    print(file.tell())  # Current cursor position
    content = file.read(10)
    print(file.tell())  # Updated cursor position after reading
