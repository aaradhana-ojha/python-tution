#Positional parameters are parameters whose values are determined by their position in the function call.
#They are matched with arguments based on their order.

def add(x, y):
    return x + y

result = add(3, 5)  # 3 is assigned to x and 5 is assigned to y
print("Result:", result)  # Output: 8