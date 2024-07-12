'''Write PushPage(url) and PopPage() methods/functions in Python to add a new webpage URL and 
delete a webpage URL from a List of webpage URLs, considering them to act as push and pop operations of 
the Stack data structure'''

def PushPage(stack, url):
    stack.append(url)
    print("Page '" + url + "' pushed onto the stack.")

def PopPage(stack):
    if not stack:
        print("Stack is empty. Cannot pop.")
        return None
    url = stack.pop()
    print("Page '" + url + "' popped from the stack.")
    return url

page_stack = []

PushPage(page_stack, "https://www.google.com")
PushPage(page_stack, "https://www.youtube.com")
PushPage(page_stack, "https://www.github.com")
PushPage(page_stack, "https://www.stackoverflow.com")

print("Current stack:", page_stack)

PopPage(page_stack)
PopPage(page_stack)
PopPage(page_stack)
PopPage(page_stack)
PopPage(page_stack)

print("Current stack:", page_stack)
