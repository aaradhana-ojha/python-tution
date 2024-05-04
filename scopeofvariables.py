# Scope of a Variable:
# Scope refers to the visibility and lifetime of a variable within a program.
# Variables can have global scope (accessible throughout the program) or local
# scope (accessible only within a specific block of code).

x = 10  # Global variable

def foo():
    y = 20  # Local variable
    print(x)  # Accessible
    print(y)  # Accessible

foo()
print(x)  # Accessible
# print(y)  # Not accessible (NameError: name 'y' is not defined)
