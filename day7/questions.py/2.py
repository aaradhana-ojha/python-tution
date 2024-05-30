def linear_search(lst, target):
    
    for index in range(len(lst)):
        
        if lst[index] == target:
            return index
        
       
    return -1

# List of numbers
lst = [10, 20, 30, 40, 50]

# Target value to search for
target = 60

# Performing linear search


print("Element found at index:", linear_search(lst, target))  # Output: Element found at index: 2
