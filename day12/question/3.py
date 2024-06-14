'''Scenario:
You are developing a Python application that needs 
to store a list of dictionaries, each containing 
information about different software packages 
(name, version, and dependencies). 
You must write Python code to serialize 
this list to a binary file and then read it back for further processing.

Task:

Serialize a list of dictionaries to a file named packages.bin.
Deserialize the list from packages.bin and print each dictionary to verify the data integrity.'''

import pickle

# Data to be serialized
software_packages = [
    {"name": "numpy", "version": "1.21.2", "dependencies": ["python>=3.6"]},
    {"name": "pandas", "version": "1.3.3", "dependencies": ["numpy", "python>=3.7"]},
    {"name": "scikit-learn", "version": "0.24.2", "dependencies": ["numpy", "scipy"]}
]

# Serialize the data
with open('packages.bin', 'wb') as file:
    pickle.dump(software_packages, file)

# Deserialize the data
with open('packages.bin', 'rb') as file:
    loaded_packages = pickle.load(file)
    print("Loaded software packages:")
    for package in loaded_packages:
        print(package)
