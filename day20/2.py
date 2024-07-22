def PushOn(stack, book_no, book_name):
    stack.append((book_no, book_name))
    print("Book '" + book_name + "' (No: " + str(book_no) + ") added to stack.")

def Display(stack):
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Stack contains:")
        for book in stack:
            print("Book No: " + str(book[0]) + ", Book Name: '" + book[1] + "'")


book_stack = []
PushOn(book_stack, 1, "The Great Gatsby")
PushOn(book_stack, 2, "1984")
Display(book_stack)


