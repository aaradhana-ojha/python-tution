def count_frequency(lst):
    '''This defines a function named 
    count_frequency that takes a list 
    lst as its parameter.'''
    frequency_dict = {}
    '''This creates an empty dictionary 
    called frequency_dict that will store 
    the count of each element.'''
    for item in lst:
        '''This loop iterates over each element in the list lst.'''
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
            '''If the element (item) is already 
            a key in frequency_dict, its value 
            (count) is incremented by 1.
            If the element is not in the dictionary, 
            it is added with a count of 1.'''
    return frequency_dict
'''The function returns the dictionary containing 
the frequency of each element.'''

# List of elements
elements = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Counting the frequency of elements
frequency = count_frequency(elements)

# Printing the frequency of elements
print("Frequency of elements:", frequency)
