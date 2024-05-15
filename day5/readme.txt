Built-in functions in Python are functions 
that are pre-defined and readily available 
for use without requiring explicit definition. 
These functions are part of the Python Standard 
Library and cover a wide range of tasks, from 
mathematical operations to data manipulation, 
file handling, input/output operations, and more. 

Type conversion functions in Python are built-in 
functions that allow you to convert data from one 
type to another.


input(prompt):

Used to take user input from the keyboard during program execution.
Optionally takes a prompt message (prompt) to display to the user.
Always returns a string, so type conversion may be needed for numeric inputs.
eval(expression):

Evaluates a Python expression (as a string) and returns the result.
Use with caution as it can execute arbitrary code. Avoid using it with untrusted inputs.
max(iterable, *iterables, key=None, default=None):

Returns the largest item in an iterable or among multiple iterables.
Optionally takes a key function for custom comparisons and a default value if the iterable is empty.
min(iterable, *iterables, key=None, default=None):

Returns the smallest item in an iterable or among multiple iterables.
Optionally takes a key function for custom comparisons and a default value if the iterable is empty.
abs(number):

Returns the absolute (positive) value of a number.
Works for integers, floats, and complex numbers.
type(object):

Returns the type of an object.
Useful for checking the data type of variables or objects.
name:

This doesn't refer to a specific built-in function but can be a variable storing a string value (e.g., name = "John").
len(s):

Returns the length (number of items) of an object.
Works with strings, lists, tuples, dictionaries, sets, and other iterable objects.
round(number[, ndigits]):

Rounds a floating-point number to a specified number of decimal digits (ndigits).
If ndigits is not provided, it rounds to the nearest integer.
range(start, stop[, step]):

Generates a sequence of numbers from start to stop (exclusive) with an optional step size.
Useful for creating sequences used in loops, list comprehensions, etc.





Importing modules in Python allows you to 
use code from other Python files or external 
libraries in your program. 

 import math

The random module in Python is a built-in module 
that provides functionalities related to generating 
random numbers, making random selections, and shuffling 
sequences. It is part of the Python Standard Library, 
so you can use it without installing any additional packages.