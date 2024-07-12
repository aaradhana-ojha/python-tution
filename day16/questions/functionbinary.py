def search_student_binary(rollno):
    try:
        with open('students.txt', 'r') as file:
            students = [line.strip().split(',') for line in file]
            students = [(int(student[0]), student[1]) for student in students]  
            
            '''with open('students.txt', 'r') as file:: This line attempts to 
            open the file students.txt in read mode ('r'). The with statement 
            is used to ensure that the file is properly closed after its suite 
            finishes, even if an exception is raised. The opened file is referenced by the variable file.
            students = [line.strip().split(',') for line in file]: This line reads each line in the file, 
            strips any leading and trailing whitespace, and splits the line into a list of strings based 
            on the comma delimiter. The result is a list of lists, where each inner list represents a 
            student's data (roll number and name). For example, if the file contains 1,To Kill a 
            Mockingbird, 2,1984, the list students will be [['1', 'To Kill a Mockingbird'], ['2', '1984']].
            students = [(int(student[0]), student[1]) for student in students]: This line converts the 
            first element (roll number) of each inner list to an integer and forms a list of tuples where 
            each tuple contains an integer roll number and a string name. The list students will be 
            [(1, 'To Kill a Mockingbird'), (2, '1984')].'''
        
        # Binary search
        left, right = 0, len(students) - 1 
        while left <= right:
            mid = (left + right) // 2
            if students[mid][0] == rollno:
                return "Student found: Roll No: " + str(students[mid][0]) + ", Name: " + students[mid][1]
            elif students[mid][0] < rollno:
                left = mid + 1
            else:
                right = mid - 1
        return "Student not found."
            '''left, right = 0, len(students) - 1: These lines initialize two pointers, left and right. left is set to 0, the start of the list, and right is set to len(students) - 1, the end of the list.
                while left <= right:: This begins a while loop that will continue as long as left is less than or equal to right.
                mid = (left + right) // 2: This line calculates the midpoint index of the current search range.
                if students[mid][0] == rollno:: This line checks if the roll number at the midpoint index is equal to the rollno we are searching for.
                return "Student found: Roll No: " + str(students[mid][0]) + ", Name: " + students[mid][1]: If the roll number matches, this line constructs a string with the roll number and the student's name, and then returns this string. The return statement exits the function immediately, so if a match is found, the rest of the lines will not be executed.
                elif students[mid][0] < rollno:: This line checks if the roll number at the midpoint index is less than the rollno we are searching for.
                left = mid + 1: If the roll number is less than rollno, this line updates the left pointer to mid + 1, narrowing the search range to the right half of the current range.
                else:: This line is executed if the roll number at the midpoint index is greater than the rollno we are searching for.
                right = mid - 1: This line updates the right pointer to mid - 1, narrowing the search range to the left half of the current range.
                return "Student not found.": If the loop completes without finding a matching roll number, this line is executed. It returns the string "Student not found.".
            '''
    
    
    except FileNotFoundError:
        return "Data file not found."


print(search_student_binary(1))  
print(search_student_binary(6))  
print(search_student_binary(3))  
