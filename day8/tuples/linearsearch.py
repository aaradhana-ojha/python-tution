def linear_search(tup, target):
    for index in range(len(tup)):
        if tup[index] == target:
            return index
    return -1

# Example tuple and target
numbers = (10, 20, 30, 40, 50)
target = 30

# Performing linear search
index = linear_search(numbers, target)
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")
'''if index != -1:: This line checks if the index 
returned by the linear_search function is not equal 
to -1. If the index is not -1, it means that the target 
value was found in the numbers tuple.

print("Element found at index:", index): If the target 
value was found in the tuple, this line prints a message 
indicating that the element was found, along with its index in the tuple.

else:: If the index is -1, it means that the target 
value was not found in the tuple.

print("Element not found"): In this case, this line 
prints a message indicating that the element was not found in the tuple.'''