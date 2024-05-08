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


'''if income <= 10000:: If the income is less than or equal to 10000, the tax is set to 0.
elif income <= 30000:: If the income is greater than 10000 but less than or equal to 30000, 
the tax is calculated as 10% of the amount exceeding 10000.
elif income <= 60000:: If the income is greater than 30000 but less 
than or equal to 60000, the tax is calculated as 10% of the first 20000 (30000 - 10000) plus 
20% of the amount exceeding 30000.
else:: For incomes exceeding 60000, the tax is calculated as 10% of the first 20000, 20% of 
the next 30000 (60000 - 30000), and 30% of the amount exceeding 60000.
Finally, print("Income Tax:", tax) prints out the calculated tax.'''