# Arbitrary argument list

def argument_list(greeting, name, *args):
    print(f'{greeting} {name}. These are your values')

    for arg in args:
        print(arg)

argument_list('Hi', 'Jenna', 'White', 'Black', 1, 2, 3,)

# Output
# Hi Jenna. These are your values
# White
# Black
# 1
# 2
# 3

# Keyword-only argument after variable argument list
def concat(*args, separator="-"):
    print(separator.join(args))

concat('air', 'water', 'fire')
# air-water-fire

concat('air', 'water', 'fire', separator="*")
# air*water*fire
