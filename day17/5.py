import pickle

def countrec():
    with open('STUDENT.DAT', 'rb') as file:
        count = 0
        while True:
            try:
                student = pickle.load(file)
                if student['Percentage'] > 75:
                    print(student)
                    count += 1
            except EOFError:
                break
        print("Number of students scoring above 75%: " + str(count))

