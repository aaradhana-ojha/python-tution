def push(stk, item):
    stk.append(item)
    print("Item '" + item + "' added to stack.")

def pop(stk):
    if len(stk) == 0:
        print("Stack is empty. Cannot pop.")
    else:
        removed_item = stk.pop()
        print("Item '" + removed_item + "' removed from stack.")

def is_empty(stk):
    return len(stk) == 0

def display(stk):
    if is_empty(stk):
        print("Stack is empty.")
    else:
        print("Stack contains:")
        for item in stk:
            print(item)


my_stack = []

while True:
    print("\nChoose an operation:")
    print("1. Push an item onto the stack")
    print("2. Pop an item from the stack")
    print("3. Display the stack")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        item = input("Enter the item to push: ")
        push(my_stack, item)
    elif choice == '2':
        pop(my_stack)
    elif choice == '3':
        display(my_stack)
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
