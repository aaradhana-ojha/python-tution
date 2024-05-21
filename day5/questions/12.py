import random

def generate_random_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def main():
    size = int(input("Enter the size of the list: "))
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    random_list = generate_random_list(size, lower_bound, upper_bound)
    print("Random list:",random_list)

if __name__ == "__main__":
    main()
