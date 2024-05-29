for num in range(45, 66):
    if num > 50 and num < 60:
        continue  # Skip numbers greater than 50 and less than 60
    if num == 60:
        break  # Stop the loop at 60
    print(num)
