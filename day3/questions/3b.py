n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    sum_evens = 0
    for i in range(2, n + 1, 2):
        sum_evens += i
    print("Sum of even numbers from 1 to", n, "is", sum_evens)



    
