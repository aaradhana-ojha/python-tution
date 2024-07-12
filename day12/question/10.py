import pickle

def add_employee_record(file_name):
    empcode = input("Enter employee code: ")
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))
    
    record = {"empcode": empcode, "name": name, "salary": salary}
    
    with open(file_name, "ab") as file:
        pickle.dump(record, file)

def display_all_employees(file_name):
    try:
        with open(file_name, "rb") as file:
            print("All Employee Records:")
            while True:
                try:
                    employee_record = pickle.load(file)
                    print("Empcode:", employee_record['empcode'], ", Name:", employee_record['name'], ", Salary:", employee_record['salary'])
                except EOFError:
                    break
    except FileNotFoundError:
        print("The file '", file_name, "' does not exist.")
    except Exception as e:
        print("An error occurred:", e)

def display_high_salary_employees(file_name):
    try:
        with open(file_name, "rb") as file:
            print("Employees with salaries between 25000 and 30000:")
            while True:
                try:
                    employee_record = pickle.load(file)
                    if 25000 < employee_record["salary"] < 30000:
                        print("Empcode:", employee_record['empcode'], ", Name:", employee_record['name'], ", Salary:", employee_record['salary'])
                except EOFError:
                    break
    except FileNotFoundError:
        print("The file '", file_name, "' does not exist.")
    except Exception as e:
        print("An error occurred:", e)

# File name
file_name = "employee.dat"

# Add a new employee record
add_employee_record(file_name)

# Display all employee records
display_all_employees(file_name)

# Display employees with salaries between 25000 and 30000
display_high_salary_employees(file_name)
