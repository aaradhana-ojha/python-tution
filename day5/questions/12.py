import random

def generate_random_numbers(n, lower_bound, upper_bound):
    
    return [random.randint(lower_bound, upper_bound) for _ in range(n)]

# Example usage
print(generate_random_numbers(5, 1, 101))  # Output: [random numbers between 1 and 100]
