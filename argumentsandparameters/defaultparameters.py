#Default parameters have a default value specified in the function definition.
#If no value is provided for a default parameter during function call, the default value is used.

def greet(name="world"):
    print("Hello,", name)

greet()  # Output: Hello, world

