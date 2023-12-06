# Exploring the content of the math module
import math

module_contents = dir(math)
print(f"Contents of the 'math' module: {module_contents}")

# Output
# Contents of the 'math' module:
# ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos',
# 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign',
# 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs',
# 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose',
# 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p',
# 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder',
# 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

# Revealing object attributes
text = "Hello, Python!"

object_attributes = dir(text)
print(f'Attributes of the string object: {object_attributes}')

# Output:
# Attributes of the string object:
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
# '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
# '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode',
# 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
# 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
# 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind',
# 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
# 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# dir() function without arguments
print(f'dir() function without arguments: {dir()}')

# Output:
# dir() function without arguments:
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', 'math',
# 'module_contents', 'object_attributes', 'text']

# Discovering built-in functions
built_in_functions = dir(__builtins__)
print(f'Built-in functions: {built_in_functions}')

# Built-in functions:
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
# 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError',
# 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
# 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
# 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception',
# 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError',
# 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
# 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
# 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError',
# 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
# 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning',
# 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError',
# 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration',
# 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError',
# 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
# 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError',
# 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__',
# '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext',
# 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr',
# 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir',
# 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset',
# 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance',
# 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min',
# 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr',
# 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum',
# 'super', 'tuple', 'type', 'vars', 'zip']

# Self-discovery for Objects
class SelfDiscoveringObject:
    def explore_self(self):
        return dir(self)

instance = SelfDiscoveringObject()
attributes = instance.explore_self()

print(f'Attributes of the instance: {attributes}')

# Attributes of the instance:
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'explore_self']

# Peering into the Global namespace
global_namespace = dir()
print(f'Global namespace: {global_namespace}')

# Global namespace:
# ['SelfDiscoveringObject', '__annotations__', '__builtins__', '__cached__', '__doc__',
# '__file__', '__loader__', '__name__', '__package__', '__spec__', 'attributes',
# 'built_in_functions', 'instance', 'math', 'module_contents', 'object_attributes',
# 'text']







