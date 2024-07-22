'''A  list contains following record of course details for a University :  
[Course_name, Fees, Duration] 
Write the following user defined functions to perform given operations on 
the stack named 'Univ' : 
(i) 
Push_element()  To push an object containing the 
Course_name, Fees and Duration of a course, which has fees 
greater than 100000 to the stack.  
(ii) 
Pop_element()  To pop the object from the stack and display it. 
 also display underflow when there is no element'''
 
def Push_element(stack, course):
    if course[1] > 100000:
        stack.append(course)
        print("Course '" + course[0] + "' added to stack.")
    else:
        print("Course '" + course[0] + "' has fees less than or equal to 100000 and was not added to the stack.")

def Pop_element(stack):
    if len(stack) == 0:
        print("Stack is empty. Underflow condition.")
    else:
        removed_course = stack.pop()
        print("Popped course: " + str(removed_course))

Univ = []

courses = [
    ["Computer Science", 120000, "4 years"],
    ["Mathematics", 95000, "3 years"],
    ["Engineering", 150000, "4 years"],
    ["History", 80000, "3 years"]
]

for course in courses:
    Push_element(Univ, course)

Pop_element(Univ)
Pop_element(Univ)
Pop_element(Univ)
Pop_element(Univ)
