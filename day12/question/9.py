'''. Given a binary file employee.dat, created using dictionary object having keys: 
(empcode, name, and salary) 
i. 
ii. 
Write a python function that add one more record at the end of file. 
Write a python function that display all employee records whose salary is more that 
30000 '''

import pickle

def add_employee_record(file_name):
    empcode = input("Enter employee code: ")
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))
    
    record = {"empcode": empcode, "name": name, "salary": salary}
    
    with open(file_name, "ab") as file:
        pickle.dump(record, file)

def display_high_salary_employees(file_name):
    with open(file_name, "rb") as file:
        print("Employees with salary more than 30,000:")
        while True:
            try:
                employee_record = pickle.load(file)
                if employee_record["salary"] > 30000:
                    print("Empcode:", employee_record["empcode"], ", Name:", employee_record["name"], ", Salary:", employee_record["salary"])
            except EOFError:
                break

# File name
file_name = "employee.dat"

# Add a new employee record
add_employee_record(file_name)

# Display employees with salary more than 30,000
display_high_salary_employees(file_name)
