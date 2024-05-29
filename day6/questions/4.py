for num in range(10, 31):
    if num % 10 == 5:
        continue  # Skip numbers ending in 5
    if num == 25:
        break  # Stop the loop at 25
    print(num)
