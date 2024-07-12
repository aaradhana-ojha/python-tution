'''Write PushCustomer(name) and PopCustomer() methods/functions in Python to add a new customer name and 
delete a customer name from a List of customer names, considering them to act as push and pop operations of 
the Stack data structure'''

def PushCustomer(stack, name):
    stack.append(name)
    print("Customer '" + name + "' pushed onto the stack.")
    
    

def PopCustomer(stack):
    if not stack:
        print("Stack is empty. Cannot pop.")
        return None
    name = stack.pop()
    print("Customer '" + name + "' popped from the stack.")
    return name


customer_stack = []

PushCustomer(customer_stack, "Alice")
PushCustomer(customer_stack, "Bob")
PushCustomer(customer_stack, "Charlie")
PushCustomer(customer_stack, "Diana")



print("Current stack:", customer_stack)


PopCustomer(customer_stack)
PopCustomer(customer_stack)
PopCustomer(customer_stack)
PopCustomer(customer_stack)
PopCustomer(customer_stack)


print("Current stack:", customer_stack)
