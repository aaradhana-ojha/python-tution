my_list = [1, 2, 3, "apple", 4.5]

# len(): Returns the number of elements in a list.
print(len(my_list))  # Output: 5

# list(): Converts an iterable into a list.
my_str = "hello"
str_to_list = list(my_str)
print(str_to_list)  # Output: ['h', 'e', 'l', 'l', 'o']

# append():Adds an element to the end of the list.
my_list.append("new")
print(my_list)  # Output: [1, 2, 3, 'apple', 4.5, 'new']

# extend(): Extends the list by appending elements from another iterable.
my_list.extend([6, 7])
print(my_list)  # Output: [1, 2, 3, 'apple', 4.5, 'new', 6, 7]

# insert():Inserts an element at a specified position.
my_list.insert(2, "inserted")
print(my_list)  # Output: [1, 2, 'inserted', 3, 'apple', 4.5, 'new', 6, 7]

# count(): Returns the number of occurrences of an element
print(my_list.count(2))  # Output: 1

# index(): Returns the index of the first occurrence of an element.
print(my_list.index('apple'))  # Output: 4

# remove(): Removes the first occurrence of an element.
my_list.remove(3)
print(my_list)  # Output: [1, 2, 'inserted', 'apple', 4.5, 'new', 6, 7]

# pop(): Removes and returns the element at the specified position.
popped_item = my_list.pop(2)
print(popped_item)  # Output: 'inserted'
print(my_list)  # Output: [1, 2, 'apple', 4.5, 'new', 6, 7]

# reverse(): Reverses the elements of the list in place.
my_list.reverse()
print(my_list)  # Output: [7, 6, 'new', 4.5, 'apple', 2, 1]

# sort(): Sorts the list in ascending order.
num_list = [3, 1, 4, 2]
num_list.sort()
print(num_list)  # Output: [1, 2, 3, 4]

# sorted(): Returns a new list that is a sorted version of the original list.
sorted_list = sorted(num_list, reverse=False)
print(sorted_list)  # Output: [4, 3, 2, 1]

# min(): Returns the smallest element in the list.
print(min(num_list))  # Output: 1

# max(): Returns the largest element in the list.
print(max(num_list))  # Output: 4

# sum(): Returns the sum of all elements in the list.
print(sum(num_list))  # Output: 10
