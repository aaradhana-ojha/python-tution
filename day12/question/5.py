'''13. A binary file "STUDENT.DAT" has structure (admission_number, Name, Percentage).
Write a function count_rec() in Python that would read contents of the file
"STUDENT.DAT" and display the details of those students whose percentage is above 75.
Also display number of students scoring above 75%'''

import pickle

def count_rec():
    count = 0
    students_above_75 = []

    try:
        with open('STUDENT.DAT', 'rb') as file:
            while True:
                try:
                    student_record = pickle.load(file)
                    if student_record["Percentage"] > 75:
                        count += 1
                        students_above_75.append(student_record)
                except EOFError:
                    break
    except FileNotFoundError:
        print("The file STUDENT.DAT does not exist.")
        return 0

    print("Students with percentage above 75%:")
    for student in students_above_75:
        print("Admission Number:", student["admission_number"], ", Name:", student["Name"], ", Percentage:", student["Percentage"])

    print("Number of students scoring above 75%:", count)
    return count

# Example usage
count_rec()
