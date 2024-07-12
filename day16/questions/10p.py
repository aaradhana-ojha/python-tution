'''Write AddOperation(operation) and UndoOperation() methods/functions 
in Python to add a new operation and undo the last operation from a 
list of operations, considering them to act as push and pop operations 
of the Stack data structure.'''

def AddOperation(stack, operation):
    stack.append(operation)
    print("Operation '" + operation + "' added to the stack.")

def UndoOperation(stack):
    if not stack:
        print("No operations to undo.")
        return None
    operation = stack.pop()
    print("Operation '" + operation + "' undone.")
    return operation

operations_stack = []

while True:
    action = input("Enter 'add' to add an operation, 'undo' to undo an operation, or 'exit' to quit: ").strip().lower()
    
    if action == 'add':
        operation = input("Enter the operation to add: ")
        AddOperation(operations_stack, operation)
    elif action == 'undo':
        UndoOperation(operations_stack)
    elif action == 'exit':
        break
    else:
        print("Invalid input. Please enter 'add', 'undo', or 'exit'.")

    print("Current operations stack:", operations_stack)
