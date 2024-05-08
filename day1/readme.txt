Immutable objects are those whose state cannot be modified after creation. 
Eg
Integers: x = 5
Floats: pi = 3.14
Strings: name = "Alice"
Tuples: coordinates = (10, 20)

Mutable Objects:
Mutable objects, on the other hand, can be modified after creation.
Eg
Lists: my_list = [1, 2, 3]
Dictionaries: my_dict = {'a': 1, 'b': 2}
Sets: my_set = {1, 2, 3}


Sets:
Sets are collections of unique elements in Python, 
and they are mutable. This means you can modify a set 
after its creation by adding or removing elements. 
However, sets themselves are unordered, so the order of 
elements within a set is not guaranteed.
Example:

my_set = {1, 2, 3}
my_set.add(4)  # Modifies the original set by adding 4 to it


Tuples:
Tuples are immutable collections of elements in Python.
Once you create a tuple, you cannot change its contents. 
Tuples are often used to represent fixed collections of items, 
such as coordinates or records.
Example:
coordinates = (10, 20)
# Trying to modify a tuple will result in an error



Strings:
Strings are immutable sequences of characters in Python. 
Once a string is created, you cannot modify its characters 
directly. Any operation that seems to modify a string actually 
creates a new string with the modified value.
Example:
name = "Alice"
# Trying to modify a string will result in creating a new string object



Lists:
Lists are mutable sequences in Python. They can hold a collection 
of items, and you can modify the list by adding, removing, or 
changing elements. Lists are ordered, meaning the order of elements 
in a list is maintained.
Example:
my_list = [1, 2, 3]
my_list.append(4)  # Modifies the original list by adding 4 to it



Dictionaries:
Dictionaries are mutable collections of key-value pairs in Python. 
You can add, remove, or modify key-value pairs in a dictionary 
after its creation. Dictionaries are unordered, meaning the 
order of key-value pairs may not be preserved.
Example:
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3  # Modifies the original dictionary by adding a new key-value pair


Membership Operators:
Python provides two membership operators: in and not in. 
These operators are used to test whether a value or variable 
is a member of a sequence (such as a string, list, tuple, or set).
    in: Returns True if the value is found in the sequence.
    not in: Returns True if the value is not found in the sequence.



Identity Operators:
Python provides two identity operators: is and is not. 
These operators are used to compare the memory locations 
of two objects to determine if they refer to the same object.
    is: Returns True if both operands refer to the same object.
    is not: Returns True if both operands do not refer to the same object.



Types of flow of execution in python.
1. Sequential Execution:
Sequential execution refers to the default behavior of Python programs, 
where statements are executed line by line, in the order in which they 
appear in the code. Each statement is executed one after the other, from top to bottom.


2. Conditional Execution:
Conditional execution involves using conditional statements 
(such as if, elif, and else) to execute certain blocks of code based on conditions. 
Depending on whether a condition evaluates to True or False, 
different blocks of code are executed.

    a. if Statement:The if statement is used to execute a block of code if a condition is True. 
    Optionally, it can be followed by one or more elif (short for "else if") statements and a 
    final else statement.


3. Iterative Execution:
Iterative execution involves executing a block of code repeatedly until a 
certain condition is met. This is typically achieved using loops, 
such as for loops and while loops.