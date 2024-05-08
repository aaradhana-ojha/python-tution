# Prompt the user to input principal amount, rate of interest, and time period
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Calculate the simple interest
simple_interest = (principal * rate * time) / 100

# Display the calculated simple interest
print("The simple interest is:", simple_interest)
