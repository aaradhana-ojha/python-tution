def Push_element(stack, course_details):
    
    if course_details[1] > 100000:
        stack.append(course_details)
        print("Course '" + course_details[0] + "' (Fees: " + str(course_details[1]) + ", Duration: " + str(course_details[2]) + " months) added to stack.")
    else:
        print("Course '" + course_details[0] + "' (Fees: " + str(course_details[1]) + ", Duration: " + str(course_details[2]) + " months) not added to stack as fees is less than or equal to 100000.")

def Pop_element(stack):
  
    if len(stack) == 0:
        print("Underflow")
    else:
        course_details = stack.pop()
        print("Course '" + course_details[0] + "' (Fees: " + str(course_details[1]) + ", Duration: " + str(course_details[2]) + " months) removed from stack.")


Univ = []


courses = [
    ["Data Science", 150000, 12],
    ["English Literature", 90000, 24],
    ["Computer Science", 120000, 48],
    ["History", 80000, 36]
]


for course in courses:
    Push_element(Univ, course)


print("\nPopping elements from the stack:")
Pop_element(Univ)
Pop_element(Univ)
Pop_element(Univ)
Pop_element(Univ)
Pop_element(Univ)
