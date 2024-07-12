# Function to push an integer into the stack  
def push_integer(stack):
    item = int(input("Enter the value of the item: "))
    stack.append(item)
    print("Pushed integer:", item)
    print("Stack after pushing integer:", stack)

# Function to push student information (rollno and name) into the stack
def push_student_info(stack):
    rollno = int(input("Enter rollno of student: "))
    name = input("Enter Name of student: ")
    item = {"rollno": rollno, "name": name}
    stack.append(item)
    print("Pushed student info:", item)
    print("Stack after pushing student info:", stack)

# Main code to demonstrate the functions
stack = []

# Pushing integer into stack
print("Pushing an integer into the stack.")
push_integer(stack)
print()

# Pushing student information into stack
print("Pushing student info into the stack.")
push_student_info(stack)
print()
