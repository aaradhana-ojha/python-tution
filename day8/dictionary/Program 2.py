# Creating a dictionary with names of employees and their salaries
employees = {'John': 50000, 'Alice': 60000, 'Bob': 55000}

# Accessing salary of an employee
employee_name = 'Alice'
if employee_name in employees:
    print("The salary of", employee_name, "is $", employees[employee_name])
else:
    print("No salary information found for", employee_name)
