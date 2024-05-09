numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Basic slicing: Extract elements from index 2 to index 5 (not including 5)
slice1 = numbers[2:5]
print(slice1)  # Output: (3, 4, 5)

# Basic slicing: Extract elements from the beginning to index 6 (not including 6)
slice2 = numbers[:6]
print(slice2)  # Output: (1, 2, 3, 4, 5, 6)

# Basic slicing: Extract elements from index 3 to the end
slice3 = numbers[3:]
print(slice3)  # Output: (4, 5, 6, 7, 8, 9, 10)

# Negative indexing and reversing: Slice from the end of the tuple (last 3 elements)
slice4 = numbers[-3:]
print(slice4)  # Output: (8, 9, 10)

# Negative indexing and reversing: Reverse the tuple using slicing
reverse_numbers = numbers[::-1]
print(reverse_numbers)  # Output: (10, 9, 8, ..., 3, 2, 1)
