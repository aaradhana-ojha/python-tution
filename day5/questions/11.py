def max_min_list(numbers):
    return max(numbers), min(numbers)

def main():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    max_num, min_num = max_min_list(numbers)
    print("The maximum of the list is", max_num)
    print("The minimum of the list is",min_num)

if __name__ == "__main__":
    main()
