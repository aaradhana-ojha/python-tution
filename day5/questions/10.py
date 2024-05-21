def product_list(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

def main():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("The product of the list is", product_list(numbers))

if __name__ == "__main__":
    main()
