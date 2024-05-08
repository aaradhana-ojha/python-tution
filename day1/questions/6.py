income = float(input("Enter the income: "))

if income <= 10000:
    tax = 0
elif income <= 30000:
    tax = (income - 10000) * 0.1
elif income <= 60000:
    tax = 20000 * 0.1 + (income - 30000) * 0.2
else:
    tax = 20000 * 0.1 + 30000 * 0.2 + (income - 60000) * 0.3

print("Income Tax:", tax)
