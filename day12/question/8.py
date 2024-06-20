import pickle

def count_rec():
    admission_number = input("Enter your Admission number: ")
    name = input("Enter your name: ")
    percentage = float(input("Enter your percentage: "))
    
    record = {"admission_number": admission_number, "Name": name, "Percentage": percentage}
    above = []


    with open("STUDENT.DAT", "ab") as file:
        pickle.dump(record, file)
    
    with open("STUDENT.DAT", "rb") as file:
        while True:
            try:
                student_record = pickle.load(file)
                if student_record["Percentage"] > 75:
                    above.append(student_record)
            except EOFError:
                break

    print("Students with percentage above 75%:")
    for student in above:
        print("Admission Number:", student["admission_number"], ", Name:", student["Name"], ", Percentage:", student["Percentage"])
    
    print("Number of students scoring above 75%:", len(above))

count_rec()
