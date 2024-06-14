import pickle

# Writing to a binary file
data = {'name': 'John', 'age': 30, 'city': 'New York'}
with open('data.bin', 'wb') as file:
    pickle.dump(data, file)

# Reading from a binary file
with open('data.bin', 'rb') as file:
    
    print(pickle.load(file))  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
