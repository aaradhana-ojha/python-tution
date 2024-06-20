import pickle

def add_record():
    record = {}
    record['empcode'] = input("Enter employee code: ")
    record['name'] = input("Enter employee name: ")
    record['salary'] = float(input("Enter employee salary: "))
    try:
        with open('employee.dat', 'ab') as file:
            pickle.dump(record, file)
    except FileNotFoundError:
        print("File not found!")
        
def display_high_salary():
    try:
        with open('employee.dat', 'rb') as file:
            while True:
                try:
                    record = pickle.load(file)
                    if record['salary'] > 30000:
                        print("Employee Code:", record['empcode'])
                        print("Name:", record['name'])
                        print("Salary:", record['salary'])
                        print()
                except EOFError:
                    break
    except FileNotFoundError:
        print("File not found!")

# Example usage
add_record()
display_high_salary()
