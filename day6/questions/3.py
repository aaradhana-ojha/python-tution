for num in range(1, 31):
    if num % 3 == 0:
        continue  # Skip multiples of 3
    if num > 15:
        break  # Stop the loop after printing 15
    print(num)
