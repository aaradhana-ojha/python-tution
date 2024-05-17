my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Updating an existing value
my_dict['age'] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Adding a new key-value pair
my_dict['job'] = 'Engineer'
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

# Using update() method
my_dict.update({'city': 'San Francisco', 'age': 32})
print(my_dict)  # Output: {'name': 'Alice', 'age': 32, 'city': 'San Francisco', 'job': 'Engineer'}

