'''Write PushItem(item) and PopItem() methods/functions in Python to add a new item and 
remove an item from a List of items, considering them to act as push and pop operations of 
the Stack data structure'''

def PushItem(stack, item):
    stack.append(item)
    print("Item '" + item + "' pushed onto the stack.")

def PopItem(stack):
    if stack==[]:
        print("Stack is empty. Cannot pop.")
        return None
    item = stack.pop()
    print("Item '" + item + "' popped from the stack.")
    return item

item_stack = []

while True:
    action = input("Enter 'push' to add an item, 'pop' to remove an item, or 'exit' to quit: ").strip().lower()
    
    if action == 'push':
        item = input("Enter the name of the item to push: ")
        PushItem(item_stack, item)
    elif action == 'pop':
        PopItem(item_stack)
    elif action == 'exit':
        break
    else:
        print("Invalid input. Please enter 'push', 'pop', or 'exit'.")

    print("Current stack:", item_stack)
