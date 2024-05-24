def product_of_list(numbers):
    product = 1
    for num in numbers:
        product =product* num
    return product

# Example usage
print(product_of_list([1, 2, 3, 4, 5])) 