'''Define a function named as search_student(rollno): where we have to pass 
rollno as an argument to check whether the given student exists or not in the datafile. 
1. do using linear search, 
2. do using binary search
'''

def search_student_linear(rollno):
    try:
        with open('students.txt', 'r') as file:
            for line in file:
                student_data = line.strip().split(',')
                if int(student_data[0]) == rollno:
                    return "Student found: Roll No: " + student_data[0] + ", Name: " + student_data[1]
        return "Student not found."
    except FileNotFoundError:
        return "Data file not found."


print(search_student_linear(1))  
print(search_student_linear(3))  