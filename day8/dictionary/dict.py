# Creating a dictionary
my_dict = {'apple': 2, 'banana': 3, 'orange': 1}
# Accessing items in the dictionary
print(my_dict['apple'])  # Output: 2
# Accessing items in the dictionary
print(my_dict['apple'])  # Output: 2
my_dict['apple'] = 5
# Traversing the dictionary
for key in my_dict:
    print(key, my_dict[key])
    
    
'''Built-in Functions/Methods for Dictionaries
len(): Returns the number of items in the dictionary.
keys(): Returns a view object that displays a list of all the keys in the dictionary.
values(): Returns a view object that displays a list of all the values in the dictionary.
items(): Returns a view object that displays a list of tuples containing key-value pairs.
get(): Returns the value of the specified key. If the key does not exist, it returns a default value.
update(): Updates the dictionary with the key-value pairs from another dictionary or iterable.
del: Deletes the item with the specified key.
clear(): Removes all items from the dictionary.
fromkeys(): Creates a new dictionary with keys from a sequence and values set to a default value.
copy(): Returns a shallow copy of the dictionary.
pop(): Removes the item with the specified key and returns its value.
popitem(): Removes the last inserted key-value pair from the dictionary and returns it as a tuple.
setdefault(): Returns the value of the specified key. If the key does not exist, it inserts the key with a specified value.
max(), min(), sorted(): These functions can be used to find the maximum, minimum, or sorted list of keys in the dictionary.'''
