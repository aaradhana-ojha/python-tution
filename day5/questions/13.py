def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# Example usage
print(sum_of_even_numbers([1, 2, 3, 4, 5, 6]))  # Output: 12
