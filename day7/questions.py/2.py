def linear_search(lst, target):
    
    for index in range(len(lst)):
        '''len(lst): This function 
        call returns the number of 
        elements in the list lst. 
        For example, if lst is 
        [10, 20, 30, 40], then 
        len(lst) returns 4.

            range(len(lst)): The range function 
            generates a sequence of numbers. When 
            called with a single argument n, range(n) 
            produces a sequence of numbers from 0 to n-1. 
            So, if len(lst) is 4, then range(len(lst)) produces 
            the sequence 0, 1, 2, 3.

            for index in range(len(lst)):: This is a for loop 
            that iterates over each number in the sequence 
            produced by range(len(lst)). During each iteration, 
            the variable index takes on the value of the next 
            number in the sequence. Thus, index will be 0 in the 
            first iteration, 1 in the second iteration, 2 in the 
            third iteration, and 3 in the fourth iteration.'''
        if lst[index] == target:
            return index
        '''Iteration 1:

index = 0
lst[0] is 10
10 is not equal to target (30)
Continue to the next iteration.
Iteration 2:

index = 1
lst[1] is 20
20 is not equal to target (30)
Continue to the next iteration.
Iteration 3:

index = 2
lst[2] is 30
30 is equal to target (30)
The condition lst[index] == target is True
The function returns index which is 2
The function terminates at this point 
because the target value 30 was found at 
index 2. The print statement then outputs: 
"Element found at index: 2".'''
    return -1
'''Using return -1 in the linear_search 
function effectively signals that the 
target value was not found in the list. It provides a clear and easily detectable way for the caller of the function to handle the "not found" case.'''

# List of numbers
numbers = [10, 20, 30, 40, 50]

# Target value to search for
target = 50

# Performing linear search
index = linear_search(numbers, target)
'''This line calls the linear_search function with two arguments: numbers and target.
numbers is the list in which we are searching for the target value.
target is the value we are looking for in the list.
The linear_search function will return the index of the target value if it is found in the list. If the target is not found, it will return -1.
The returned value is then assigned to the variable index'''
print("Element found at index:", index)  # Output: Element found at index: 2
