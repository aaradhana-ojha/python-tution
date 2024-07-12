def PushTab(stack, tab):
    stack.append(tab)
    print("Tab '" + tab + "' pushed onto the stack.")

def PopTab(stack):
    if not stack:
        print("Stack is empty. Cannot pop.")
        return None
    tab = stack.pop()
    print("Tab '" + tab + "' popped from the stack.")
    return tab

tab_stack = []

while True:
    action = input("Enter 'push' to add a tab, 'pop' to remove a tab, or 'exit' to quit: ").strip().lower()
    
    if action == 'push':
        tab = input("Enter the name of the tab to push: ")
        PushTab(tab_stack, tab)
    elif action == 'pop':
        PopTab(tab_stack)
    elif action == 'exit':
        break
    else:
        print("Invalid input. Please enter 'push', 'pop', or 'exit'.")

    print("Current stack:", tab_stack)
