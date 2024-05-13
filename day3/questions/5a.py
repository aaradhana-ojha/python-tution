num = int(input("Enter a number: "))
factorial = 1
counter = 1

while counter <= num:
    factorial *= counter
    counter += 1

print("The factorial of", num, "is", factorial)
