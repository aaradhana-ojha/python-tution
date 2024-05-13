num = int(input("Enter a positive integer: "))
sum_even = 0
current_num = 2

while current_num <= num:
    sum_even += current_num
    current_num += 2

print("The sum of all even numbers from 1 to", num, "is", sum_even)
