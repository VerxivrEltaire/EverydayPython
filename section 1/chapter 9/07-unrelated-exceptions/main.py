# Exception group
def f():
    excs = [OSError('exception error 1'), SystemError('exception error 2')]
    raise ExceptionGroup('there were code problems', excs)

f()

# + Exception Group Traceback (most recent call last):
#   |   File "07-unrelated-exceptions/main.py", line 6, in <module>
#   |     f()
#   |   File "/07-unrelated-exceptions/main.py", line 4, in f
#   |     raise ExceptionGroup('there were problems', excs)
#   | ExceptionGroup: there were problems (2 sub-exceptions)
#   +-+---------------- 1 ----------------
#     | OSError: error 1
#     +---------------- 2 ----------------
#     | SystemError: error 2
#     +------------------------------------

# Selecting exceptions with excerpt*
def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1), SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3), RecursionError(4)
                ]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("OSErrors occurred")
except* SystemError as e:
    print("SystemErrors occurred")

# + Exception Group Traceback (most recent call last):
#   |   File "/07-unrelated-exceptions/main.py", line 36, in <module>
#   |     f()
#   |   File "/07-unrelated-exceptions/main.py", line 22, in f
#   |     raise ExceptionGroup(
#   | ExceptionGroup: group1 (1 sub-exception)
#   +-+---------------- 1 ----------------
#     | ExceptionGroup: group2 (1 sub-exception)
#     +-+---------------- 1 ----------------
#       | RecursionError: 4
#       +------------------------------------

# Nested exceptions
excs = []
for execute in values:
    try:
        execute.run()
    except Exception as e:
        excs.append(e)

if excs:
   raise ExceptionGroup("Execution Failures", excs)