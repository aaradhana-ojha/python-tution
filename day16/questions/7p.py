'''Write PushTab(tab) and PopTab() methods/functions in Python to add a new browser tab and 
delete a browser tab from a List of browser tabs, considering them to act as push and pop operations of 
the Stack data structure'''

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

PushTab(tab_stack, "Tab 1: Google")
PushTab(tab_stack, "Tab 2: YouTube")
PushTab(tab_stack, "Tab 3: GitHub")
PushTab(tab_stack, "Tab 4: StackOverflow")

print("Current stack:", tab_stack)

PopTab(tab_stack)
PopTab(tab_stack)
PopTab(tab_stack)
PopTab(tab_stack)
PopTab(tab_stack)

print("Current stack:", tab_stack)
