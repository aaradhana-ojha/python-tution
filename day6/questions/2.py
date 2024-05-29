for num in range(1, 21):
    if num % 2 == 0:
        continue  # Skip even numbers
    if num % 7 == 0:
        break  # Stop the loop if the number is a multiple of 7
    print(num)
