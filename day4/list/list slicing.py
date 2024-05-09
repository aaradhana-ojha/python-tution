# List slicing examples

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic slicing: Extract elements from index 2 to index 5 (not including 5)
slice1 = numbers[2:5]
print(slice1)  # Output: [3, 4, 5]

# Basic slicing: Extract elements from the beginning to index 6 (not including 6)
slice2 = numbers[:6]
print(slice2)  # Output: [1, 2, 3, 4, 5, 6]

# Basic slicing: Extract elements from index 3 to the end
slice3 = numbers[3:]
print(slice3)  # Output: [4, 5, 6, 7, 8, 9, 10]

# Negative indexing and reversing: Slice from the end of the list (last 3 elements)
slice4 = numbers[-3:]
print(slice4)  # Output: [8, 9, 10]

# Negative indexing and reversing: Reverse the list using slicing
reverse_numbers = numbers[::-1]
print(reverse_numbers)  # Output: [10, 9, 8, ..., 3, 2, 1]

# Slicing with step size: Extract every second element
slice5 = numbers[::2]
print(slice5)  # Output: [1, 3, 5, 7, 9]

# Slicing with step size: Reverse the list with step size 2
reverse_step = numbers[::-2]
print(reverse_step)  # Output: [10, 8, 6, 4, 2]

# Modifying elements via slicing: Modify elements in a slice
numbers[1:4] = [20, 30, 40]
print(numbers)  # Output: [1, 20, 30, 40, 5, 6, 7, 8, 9, 10]
