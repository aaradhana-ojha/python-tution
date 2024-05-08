x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)    # Output: False (different objects, even though they have the same content)
print(x is z)    # Output: True (x and z refer to the same object)
print(x is not y)   # Output: True (x and y do not refer to the same object)
