# Assigning the result of a comparison or Boolean to a variable
str1, str2, str3 = '', 'Abuja', 'Calabar carnival'
non_null = str1 or str2 or str3

print(non_null)  # Output: 'Abuja'

# Using the walrus operator

# Example demonstrating the walrus operator
data = [26.5, float('NaN'), 31.6, 65.4, float('NaN'), 12.9, float('NaN'), 87.2]

if (count := len(data)) > 0:
    print(f'The data has {count} elements.')
else:
    print('No elements in the data.')

# Output: The data has 8 elements.
