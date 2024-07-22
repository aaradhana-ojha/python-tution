def PushOn(stack, book_title):
    stack.append(book_title)
    print("Book '" + book_title + "' added to stack.")

def Pop(stack):
    if len(stack) == 0:
        print("Stack is empty. Cannot pop.")
    else:
        removed_book = stack.pop()
        print("Book '" + removed_book + "' removed from stack.")


book_stack = []
PushOn(book_stack, "The Great Gatsby")
PushOn(book_stack, "1984")
Pop(book_stack)
Pop(book_stack)
Pop(book_stack)
