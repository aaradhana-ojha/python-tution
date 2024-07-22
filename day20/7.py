'''Visit Page: Write a function VisitPage(history, page_url) that adds a page URL to the history stack.
Go Back: Write a function GoBack(history) that removes and returns the most recently visited page from the history stack. If the history stack is empty, print a message indicating that there are no pages to go back to.'''


'''Visit Page: Write a function VisitPage(history, page_url) that adds a page URL to the history stack.
Go Back: Write a function GoBack(history) that removes and returns the most recently visited page from the history stack. If the history stack is empty, print a message indicating that there are no pages to go back to.'''


def VisitPage(history, page_url):
    history.append(page_url)
    print("Visited page: " + page_url)

def GoBack(history):
    if len(history) == 0:
        print("No pages to go back to.")
    else:
        previous_page = history.pop()
        print("Going back to: " + previous_page)

history = []
VisitPage(history, "https://example.com")
VisitPage(history, "https://example.com/about")
GoBack(history)
GoBack(history)
GoBack(history)

