import pickle

def count_rec():
    count = 0
    try:
        with open('STUDENT.DAT', 'rb') as file:
            while True:
                try:
                    record = pickle.load(file)
                    if record[2] > 75:
                        print("Admission Number:", record[0])
                        print("Name:", record[1])
                        print("Percentage:", record[2])
                        print()
                        count += 1
                except EOFError:
                    break
    except FileNotFoundError:
        print("File not found!")
    print("Number of students scoring above 75%:", count)

# Example usage
count_rec()
