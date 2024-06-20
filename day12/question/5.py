'''13. A binary file "STUDENT.DAT" has structure (admission_number, Name, Percentage).
Write a function count_rec() in Python that would read contents of the file
"STUDENT.DAT" and display the details of those students whose percentage is above 75.
Also display number of students scoring above 75%'''

import pickle

# Function to create a binary file with sample data
def create_file():
    students = [
        {"admission_number": 1, "Name": "John Doe", "Percentage": 85},
        {"admission_number": 2, "Name": "Jane Smith", "Percentage": 78},
        {"admission_number": 3, "Name": "Emily Davis", "Percentage": 65},
        {"admission_number": 4, "Name": "Michael Brown", "Percentage": 90},
        {"admission_number": 5, "Name": "Jessica Taylor", "Percentage": 72}
    ]
    
    with open("STUDENT.DAT", 'wb') as file:
        for student in students:
            pickle.dump(student, file)


def count_rec():
    count = 0
    students_above_75 = []

    with open("STUDENT.DAT", 'rb') as file:
        while True:
            try:
                student_record = pickle.load(file)
                if student_record["Percentage"] > 75:
                    count += 1
                    students_above_75.append(student_record)
            except EOFError:
                break

    print("Students with percentage above 75%:")
    for student in students_above_75:
        print("Admission Number:", student["admission_number"], ", Name:", student["Name"], ", Percentage:", student["Percentage"])

    print("Number of students scoring above 75%:", count)
    return count


create_file()

count_rec()
