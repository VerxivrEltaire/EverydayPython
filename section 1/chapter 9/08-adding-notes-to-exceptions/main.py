# Adding notes to exceptions
# try:
#     raise ValueError('bad value')
# except Exception as e:
#     e.add_note('Adding some value information')
#     e.add_note('Adding some more value information')
#     raise

# Traceback (most recent call last):
#   File "/08-adding-notes-to-exceptions/main.py", line 3, in <module>
#     raise ValueError('bad value')
# ValueError: bad value
# Adding some value information
# Adding some more value information

# Adding notes to exception groups
def f():
    raise OSError('operation failed to execute')

excs = []
for i in range(2):
    try:
        f()
    except Exception as e:
        e.add_note(f'Failure occurred in iteration {i+1}')
        excs.append(e)

raise ExceptionGroup('Problems exist', excs)

# + Exception Group Traceback (most recent call last):
#   |   File "/08-adding-notes-to-exceptions/main.py", line 28, in <module>
#   |     raise ExceptionGroup('Problems exist', excs)
#   | ExceptionGroup: Problems exist (2 sub-exceptions)
#   +-+---------------- 1 ----------------
#     | Traceback (most recent call last):
#     |   File "/08-adding-notes-to-exceptions/main.py", line 23, in <module>
#     |     f()
#     |   File "/08-adding-notes-to-exceptions/main.py", line 18, in f
#     |     raise OSError('operation failed to execute')
#     | OSError: operation failed to execute
#     | Failure occurred in iteration 1
#     +---------------- 2 ----------------
#     | Traceback (most recent call last):
#     |   File "/08-adding-notes-to-exceptions/main.py", line 23, in <module>
#     |     f()
#     |   File "/08-adding-notes-to-exceptions/main.py", line 18, in f
#     |     raise OSError('operation failed to execute')
#     | OSError: operation failed to execute
#     | Failure occurred in iteration 2
#     +------------------------------------