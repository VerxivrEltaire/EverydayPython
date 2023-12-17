# Pre-defined cleanup actions
for line in open("myfile.txt"):
    print(line, end="")

# with statement
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
