def showGrades(S):
    for name, marks in S.items():
        average = sum(marks) / len(marks)
        if average >= 90:
            grade = 'A'
        elif 90 > average >= 60:
            grade = 'B'
        else:
            grade = 'C'
        print(name + " - " + grade)

# Example Usage
S = {"AMIT": [92, 86, 64], "NAGMA": [65, 42, 43], "DAVID": [92, 90, 88]}
showGrades(S)
