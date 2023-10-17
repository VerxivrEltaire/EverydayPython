# 1. str.upper() and str.lower():
text = "Hello, World!"
uppercase_text = text.upper()
lowercase_text = text.lower()

print(uppercase_text)  # "HELLO, WORLD!"
print(lowercase_text)  # "hello, world!"

# 2. str.strip(), str.lstrip(), and str.rstrip():
text = "   Hello, World!   "
stripped_text = text.strip()

print(stripped_text)  # "Hello, World!"

# 3. str.startswith() and str.endswith():
text = "Hello, World!"
starts_with_hello = text.startswith("Hello")  # True
ends_with_world = text.endswith("World!")     # True

# 4. str.replace():
text = "Hello, World!"
new_text = text.replace("World", "Python")

print(new_text)  # "Hello, Python!"

# 5. str.find() and str.index():
text = "Hello, World!"
index1 = text.find("World")  # 7
index2 = text.index("World")  # 7
index3 = text.find("Python")  # -1 (not found)

print(index1, index2, index3)

# 6. str.split():
text = "Python,Java,C++,JavaScript"
languages = text.split(",")

print(languages)  # ['Python', 'Java', 'C++', 'JavaScript']

# 7. str.join():
languages = ['Python', 'Java', 'C++', 'JavaScript']
text = ",".join(languages)

print(text)  # "Python,Java,C++,JavaScript"



















