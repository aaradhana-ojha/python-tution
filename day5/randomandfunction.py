import random

def roll_die():
    return random.randint(1, 6)


# Roll the die 5 times and print the results
for i in range(5):
    
    print("You rolled a", roll_die())
