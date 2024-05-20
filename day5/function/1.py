def add_numbers(a, b):
    sum = a + b
    return sum
print("add",add_numbers(5, 3))
print("add",add_numbers(15, 30))

def subtract_numbers(a, b):
    difference = a - b
    return difference

print("sub",subtract_numbers(10, 3))  # Output: 7
print("sub",subtract_numbers(20, 5))  # Output: 15


def multiply_numbers(a, b):
    product = a * b
    return product

print(multiply_numbers(4, 5))  # Output: 20
print(multiply_numbers(7, 6))  # Output: 42


def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    quotient = a / b
    return quotient

print(divide_numbers(10, 2))  # Output: 5.0
print(divide_numbers(9, 3))   # Output: 3.0
print(divide_numbers(5, 0))   # Output: Cannot divide by zero


def max_number(a, b):
    if a > b:
        return a
    else:
        return b

print(max_number(10, 20))  # Output: 20
print(max_number(5, 3))    # Output: 5


def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even_or_odd(4))  # Output: Even
print(is_even_or_odd(7))  # Output: Odd
