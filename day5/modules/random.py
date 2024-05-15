import random

# Generate a random integer within a range
random_num = random.randint(1, 100)
print("Random number between 1 and 100:", random_num)

# Generate a random floating-point number within a range
random_float = random.uniform(1.0, 10.0)
print("Random floating-point number between 1.0 and 10.0:", random_float)

# Generate a random element from a sequence
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
random_fruit = random.choice(fruits)
print("Random fruit:", random_fruit)

# Shuffle a list randomly
random.shuffle(fruits)
print("Shuffled fruits:", fruits)
