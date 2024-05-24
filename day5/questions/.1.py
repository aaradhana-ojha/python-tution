import random

def generate_random_numbers(n, lower_bound, upper_bound):
    random_numbers = []
    for i in range(n):
        rand_num = random.randint(lower_bound, upper_bound)
        random_numbers.append(rand_num)
    return random_numbers

# Example usage
print(generate_random_numbers(5, 1, 100))  # Output: [random numbers between 1 and 100]
