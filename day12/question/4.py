'''12. A binary file "Book.dat" has structure [BookNo, Book_Name, Author, Price].
i. Write a user defined function createFile() to input data for a record and add to
Book.dat.
ii. Write a function countRec(Author) in Python which accepts the Author name as
parameter and count and return number of books by the given Author are stored in the
binary file "Book.dat"'''

import pickle

def createFile():
    book_no = input("Enter Book Number: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author: ")
    price = float(input("Enter Price: "))

    book_record = {
        "BookNo": book_no,
        "Book_Name": book_name,
        "Author": author,
        "Price": price
    }

    with open('Book.dat', 'ab') as file:
        pickle.dump(book_record, file)
    print("Book record added to Book.dat")

def countRec(author_name):
    count = 0
    books_by_author = []
    '''count is initialized to 0 to keep track of the number of books by the specified author.
books_by_author is initialized as an empty list to store the book records by the specified author.'''

    try:
        with open('Book.dat', 'rb') as file:
            while True:
                try:
                    book_record = pickle.load(file)
                    if book_record["Author"] == author_name:
                        count += 1
                        books_by_author.append(book_record)
                except EOFError:
                    break
                '''This block tries to open the file Book.dat in read-binary mode ('rb'). If the file does not exist, it will raise a FileNotFoundError.
A while True loop is used to read all the records in the file until the end of the file is reached.
Inside the loop, pickle.load(file) deserializes the next object from the file and assigns it to book_record.
The if statement checks if the Author field of book_record matches author_name. If it does, count is incremented by 1 and the book_record is appended to the books_by_author list.
An EOFError is raised when the end of the file is reached, which breaks the loop.'''
    except FileNotFoundError:
        print("The file Book.dat does not exist.")
        return 0
    '''If the file Book.dat does not exist, this block catches the FileNotFoundError and prints an error message.
The function returns 0, indicating that no records were found.'''

    for book in books_by_author:
        print("BookNo:", book["BookNo"], ", Book_Name:", book["Book_Name"], ", Author:", book["Author"], ", Price:", book["Price"])

    return count
'''This block iterates over the books_by_author list and prints the details of each book record.'''

# Example usage of createFile
print("Add a new book record:")
createFile()

# Example usage of countRec
author_to_search = input("Enter Author Name to search: ")
number_of_books = countRec(author_to_search)
print("Number of books by", author_to_search, ":", number_of_books)

