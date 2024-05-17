What is a List?
A list in Python is a collection of items (elements) that are ordered and mutable.
Lists can contain elements of different data types, including integers, floats, strings, and even other lists.
Lists are defined using square brackets [] and elements are separated by commas.

list slicing:
List slicing in Python allows you to create a new list by extracting a portion of elements from an existing list. 
It follows the syntax list[start:stop:step], where:

start: Starting index of the slice (inclusive, default is 0).
stop: Ending index of the slice (exclusive, default is the length of the list).
step: Step size for slicing (default is 1).


Tuple in Python:
A tuple in Python is a collection of ordered and immutable elements.
Tuples are defined using parentheses () and elements are separated by commas.
Unlike lists, tuples cannot be modified (immutable), which means you cannot add, remove, or modify elements 
once the tuple is created.


Tuple Slicing:
Tuple slicing allows you to create a new tuple by extracting a portion of elements from an existing tuple.

syntax:
new_tuple = old_tuple[start:stop:step]
old_tuple: The original tuple from which elements will be sliced.
    start: Optional. The starting index of the slice (inclusive). 
    If omitted, it defaults to the beginning of the tuple (0 index).
    stop: Optional. The ending index of the slice (exclusive). If omitted, 
    it defaults to the end of the tuple (length of the tuple).
    step: Optional. The step size for slicing. If omitted, it defaults to 1, 
    meaning every element in the specified range is included.


Dictionary:

A dictionary in Python is a data structure that stores key-value pairs. It's similar 
to a real-world dictionary where you look up a word (the key) to find its definition (the value).
Syntax:
            # Creating an empty dictionary
        my_dict = {}

        # Creating a dictionary with initial values
        my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
Iterating through dictionary:
    We can iterate through a dictionary using loops like for loops.


Sorting
Bubble sort: https://clementmihailescu.github.io/Sorting-Visualizer/
inserton sort: 
    

num = 3

# Loop from 1 to 10 to print the multiplication table
for i in range(1, 11):
    result = num * i
    print(num, 'x', i, '=', result)

wap to print first 10 integers and their squres using while loop only
    # Initialize the counter
num = 1

# Loop until we reach 10
while num <= 10:
    # Calculate the square
    square = num ** 2
    # Print the number and its square
    print("Number:", num, ", Square:", square)
    # Increment the counter
    num += 1


wap to print loop for series 10, 20, 30 ,40 ..., 100 using simple while and for loop only

using while 
num = 10  # Start value

# Using a while loop to print the series
while num <= 100:
    print(num, end=' ')  # Print the number
    num += 10  # Increment by 10 for the next number


using for

# Using a for loop to print the series
for num in range(10, 101, 10):
    print(num, end=' ')  # Print the number
