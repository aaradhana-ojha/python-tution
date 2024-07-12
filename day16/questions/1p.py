'''Write PushPlate(color) and PopPlate() methods/functions in Python to add a new plate color and 
delete a plate color from a List of plate colors, considering them to act as push and pop operations of 
the Stack data structure'''

def PushPlate(stack, color):
    stack.append(color)
    print("Plate with color '" + color + "' pushed onto the stack.")
    
   

def PopPlate(stack):
    if not stack:
        print("Stack is empty. Cannot pop.")
        return None
    color = stack.pop()
    print("Plate with color '" + color + "' popped from the stack.")
    return color


plate_stack = []


PushPlate(plate_stack, "Red")
PushPlate(plate_stack, "Blue")
PushPlate(plate_stack, "Green")
PushPlate(plate_stack, "Yellow")


print("Current stack:", plate_stack)


PopPlate(plate_stack)
PopPlate(plate_stack)
PopPlate(plate_stack)
PopPlate(plate_stack)
PopPlate(plate_stack)


print("Current stack:", plate_stack)
