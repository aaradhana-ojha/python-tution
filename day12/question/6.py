import pickle

def count_rec():
    # Taking input from the user
    admission_number = input("Enter your Admission number: ")
    name = input("Enter your name: ")
    percentage = float(input("Enter your percentage: "))
    
    # Create a student record
    record = {"admission_number": admission_number, "Name": name, "Percentage": percentage}
    
    # Write the record to the binary file
    with open("STUDENT.DAT", "ab") as file:
        pickle.dump(record, file)
    
    # Read records from the file and display those with percentage above 75%
    count = 0
    students_above_75 = []
    
    with open("STUDENT.DAT", "rb") as file:
        while True:
            try:
                student_record = pickle.load(file)
                if student_record["Percentage"] > 75:
                    count += 1
                    students_above_75.append(student_record)
            except EOFError:
                break
    
    # Display the students with percentage above 75%
    print("Students with percentage above 75%:")
    for student in students_above_75:
        print("Admission Number:", student["admission_number"], ", Name:", student["Name"], ", Percentage:", student["Percentage"])
    
    # Display the count of students scoring above 75%
    print("Number of students scoring above 75%:", count)

# Call the function
count_rec()
