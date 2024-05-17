result = eval("2 + 3 * 4")
print(result)  # Output: 14

'''The eval() function in Python 
evaluates the specified expression,
which is passed to it as a string, 
and returns the result. It can execute a 
dynamically created string-based expression 
and compute its value.'''


# Basic arithmetic
result1 = eval("10 / 2 + 5")
print(result1)  # Output: 10.0

# Using variables
x = 10
y = 5
result2 = eval("x * y - 3")
print(result2)  # Output: 47

# Complex expressions
result3 = eval("2**3 + (4 * 2) / 2")
print(result3)  # Output: 10.0
