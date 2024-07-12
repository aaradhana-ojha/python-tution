'''A binary file "Employee.dat" has structure [EmpNo, EmpName, Post, sal].
i. Write a user defined function CreateFile() to input data for a record and add to Employee.dat
ii. Write a function CountRec(Post) in Python which accepts the Post as parameter and count and return the number of employees working under this post (records should be stored in "Employee.dat")'''
import pickle

def CreateFile():
    with open("Employee.dat", "ab") as f:
        emp_no = int(input("Enter EmpNo: "))
        emp_name = input("Enter EmpName: ")
        post = input("Enter Post: ")
        sal = float(input("Enter Salary: "))
        record = [emp_no, emp_name, post, sal]
        pickle.dump(record, f)

def CountRec(post):
    count = 0
    with open("Employee.dat", "rb") as f:
        try:
            while True:
                record = pickle.load(f)
                if record[2] == post:
                    count += 1
        except EOFError:
            pass
    return count

# Example usage
CreateFile()
print("Number of employees in post 'Manager':", CountRec('Manager'))
