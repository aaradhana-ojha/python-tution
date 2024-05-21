def sum_list(numbers):
    return sum(numbers)

def main():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("The sum of the list is", sum_list(numbers))

if __name__ == "__main__":
    main()
