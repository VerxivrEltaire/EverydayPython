# Creating strings
print('Hello, I am a single-quote string.')
print("Hi, I am a double-quote string.")

# Quoting in Python
print('He said "She has not come".')
# He said "She has not come".

print("She doesn't have it.")
# She doesn't have it.

# Multiple line strings
print("""\
This is a multi-line string
    - Used to display multiple texts
    - Handy for long notes
""")

# String concatenation
print('Hello ' + 'World')
# Hello World

# Automatic concatenation
print('We have some very very long strings '
      'that need to be concatenated or joined. '
      'We achieve this by placing them next to each other')

# Special characters
print('This is the first line.\nThis is the second line')
# This is the first line.
# This is the second line


# Raw strings
print('D:\mydrive\name')
# D:\mydrive
# ame

print(r'D:\mydrive\name')  # note the r before the quote
# C:\some\name

# String repetition
print('He is a ' + 3 * 'jolly ' + 'fellow')
# He is a jolly jolly jolly fellow
