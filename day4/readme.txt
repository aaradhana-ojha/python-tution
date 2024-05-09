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
