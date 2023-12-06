# my_package package

# my_package/
# |-- __init__.py
# |-- module1.py
# |-- module2.py

# from my_package import module1, module2

# module1.say_hello()
# module2.perform_task()

# Nesting packages

# my_package/
# |-- __init__.py
# |-- module1.py
# |-- subpackage/
# |   |-- __init__.py
# |   |-- module3.py
# |   |-- module4.py

# Importing from subpackages

# from my_package.subpackage import module3, module4
#
# module3.execute_action()
# module4.display_result()

# The init.py file

# __init__.py in my_package
print("Initializing my_package")

# Now, when the package is imported, the initialization code runs

# The requests package

import requests

response = requests.get("https://www.example.com")
print(response.status_code)
