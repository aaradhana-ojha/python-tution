# Stack implementation using list
stack = []
'''This line initializes an empty list called stack. 
In Python, a list can be used to implement a stack 
data structure because it supports dynamic resizing 
and provides methods to add and remove elements from both ends.'''

# Function to check if the stack is empty
def is_empty(stack):
    return len(stack) == 0

'''This defines a function is_empty that takes a 
stack (list) as an argument and returns True if 
the stack is empty (i.e., its length is zero) and 
False otherwise. The len function returns the number 
of elements in the list.'''

# Adding elements to the stack
stack.append(10)
stack.append(20)
stack.append(30)

'''These lines add three elements to the stack 
using the append method. The append method adds 
an element to the end of the list. In the context 
of a stack, this operation is called "push".'''

print("Stack after pushing elements:", stack)

# Checking if stack is empty
print("Is stack empty?", is_empty(stack))

# Removing elements from the stack
print("Popped element:", stack.pop())
'''This line removes the top element from 
the stack and prints it. The pop method 
removes and returns the last element of 
the list. In the context of a stack, 
this operation is called "pop".'''
print("Stack after popping an element:", stack)

# Traversing the stack
print("Traversing stack elements:")
for element in stack:
    print(element)
    
'''This prints each element in the 
stack by iterating over the stack 
using a for loop. This traversal 
allows you to see all elements 
currently in the stack.'''
