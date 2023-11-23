# Special parameter definition.

def f(positional1, positional2, /, positional_or_keyword, *, keyword1, keyword2):
    pass

# Positional-only parameters
def pos_only_arg(arg, /):
    print(arg)

# Keyword-only parameters
def kwd_only_arg(*, arg):
    print(arg)

# combined parameters
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
