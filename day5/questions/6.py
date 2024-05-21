import random

def fill_list_with_random_numbers(size):
    """
    Generates a list filled with random numbers between 1 and 100.

    :param size: Number of random numbers to generate.
    :return: List of random numbers.
    """
    random_numbers = []  # Initialize an empty list to store the random numbers
    for _ in range(size):  # Loop 'size' times
        random_numbers.append(random.randint(1, 100))  # Generate a random number between 1 and 100 and append it to the list
    return random_numbers  # Return the list of random numbers

# Generate and print random numbers
size = 10  # Number of random numbers to generate
random_numbers = fill_list_with_random_numbers(size)  # Call the function and store the result in 'random_numbers'
print(random_numbers)  # Print the list of random numbers
