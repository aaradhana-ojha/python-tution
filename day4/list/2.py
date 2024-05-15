fruits = ['apple', 'banana', 'cherry']

print(fruits[0])    # Output: 'apple'
print(fruits[-1])   # Output: 'cherry'
print(fruits[1:3])   # Output: ['banana', 'cherry']

'''fruits[0]: This accesses the first element of the list, 
which is 'apple'. In Python, indexing starts at 0, so [0] refers to the first element.

fruits[-1]: Negative indexing allows you to access elements 
from the end of the list. [-1] accesses the last element, which is 'cherry' in this case.

fruits[1:3]: This is a slice operation that accesses elements from index 1 
(inclusive) to index 3 (exclusive). So, it accesses 'banana' at index 1 and 'cherry' 
at index 2, but it does not include the element at index 3. The result is ['banana', 'cherry'].'''


'''Index:    0        1         2
          |        |         |
fruits = ['apple', 'banana', 'cherry']
                     ↑         ↑
                  fruits[1]  fruits[2]'''
