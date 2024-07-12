import pickle

def addrecords():
    with open('employee.dat', 'wb') as fw:
        ch = 'y'
        while ch == 'y':
            eno = int(input("Enter employee number: "))
            nm = input("Enter employee name: ")
            sal = int(input("Enter employee salary: "))
            record = {'empno': eno, 'name': nm, 'salary': sal}
            pickle.dump(record, fw)
            ch = input("Add more record? (y/n): ")

def display():
    with open('employee.dat', 'rb') as fr:
        while True:
            try:
                record = pickle.load(fr)
                print(record)
            except EOFError:
                break

