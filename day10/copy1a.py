try:
    '''This line marks the beginning of a try...except block.
It's a common error handling construct in Python that attempts to execute the code within the try block.
If an exception (an error) occurs during the execution, control jumps to the except block(s) to handle the error gracefully.'''
    # Add content to file A (assuming it exists)
    with open('file_A.txt', 'a') as file_A:  # Use 'a' for appending
        content_to_add = "This is the new content added to file A.\n"  # Replace with your desired content
        file_A.write(content_to_add)
        
        '''Line 2: This line is a comment explaining the purpose of the following code block (appending content to file_A.txt).
                Line 3:
                with open('file_A.txt', 'a') as file_A::
                This is a context manager using with open. It opens the file named file_A.txt in append mode ('a').
                'a' means that if the file doesn't exist, it will be created. If it exists, any new content you write will 
                be appended to the end of the existing content.
                The as file_A: part assigns the opened file object to the variable file_A.
                
                Line 4:
                content_to_add = "This is the new content added to file A.\n":
                This line defines a variable content_to_add and assigns a string value representing the content you want to append to file_A.txt.
                The \n at the end adds a newline character to the content.
                Line 5:
                file_A.write(content_to_add):
                This line calls the write method on the file_A object. The write method writes the content stored in the content_to_add variable to the opened file.'''

    # Open file A for reading
    with open('file_A.txt', 'r') as file_A:
        data = file_A.read()
        
        '''Line 6: This line is another comment explaining the purpose of the following code block (reading the content of file_A.txt).
            Line 7:
            with open('file_A.txt', 'r') as file_A::
            This line opens the file named file_A.txt in read mode ('r'). Read mode allows you to access the existing content of the file.
            The opened file object is assigned to the variable file_A for convenient access.
            Line 8:
            data = file_A.read():
            This line calls the read method on the file_A object. The read method reads the entire content of the file (including any previously appended content from lines 2-5) and stores it in the data variable.'''

    # Create file B (if it doesn't exist) and open it for writing
    with open('file_B.txt', 'w') as file_B:
        file_B.write(data)
        
        '''Line 10: This line is a comment explaining the purpose of the following code block (creating or writing to file_B.txt).
            Line 11:
            with open('file_B.txt', 'w') as file_B::
            This line opens the file named file_B.txt in write mode ('w').
            'w' means that if the file doesn't exist, it will be created. If it exists, its existing content will be overwritten.
            The opened file object is assigned to the variable file_B.
            Line 12:
            file_B.write(data):
            This line calls the write method on the file_B object. The write method writes the entire 
            content stored in the data variable (which contains the content read from file_A.txt in line 8) to `file_B'''

    print("Data copied successfully from file A to file B.")
    
    '''This line prints a success message to the console if the previous code blocks executed without errors.
    It indicates that the content has been appended to file_A.txt (if it existed) or written to a newly created 
    file_A.txt, and then the entire content (including the appended data) has been copied to file_B.txt.'''

    # Open file B for reading and print its content (optional)
    with open('file_B.txt', 'r') as file_B:
        print("Content of file B:")
        print(file_B.read())
        
        '''This code block is optional and provides a way to verify that the copy operation was successful.
            Line 17: This line is a comment explaining the purpose of the following code 
            (reading and printing the content of file_B.txt).
            Line 18:
            with open('file_B.txt', 'r') as file_B::
            This line opens the file named file_B.txt in read mode ('r').
            It assumes that file_B.txt has been created or overwritten with the content from 
            file_A.txt in the previous lines.
            The opened file object is assigned to the variable file_B for access.
            Line 19:
            print("Content of file B:"):
            This line prints a message to the console indicating that the content of 
            file_B.txt will be displayed.
            Line 20:
            print(file_B.read()):
            This line calls the read method on the file_B object. The read method reads 
            the entire content of file_B.txt (which should now contain the appended content 
            from file_A.txt) and prints it to the console.'''

except FileNotFoundError:
    print("One of the files doesn't exist. Please check the filenames and try again.")
    
    '''This except block handles the specific case of a FileNotFoundError.
If any of the file opening operations (in lines 3 or 7) raise a FileNotFoundError, this block will catch it.
The error message provides feedback to the user, suggesting they check the filenames and try again.'''

except Exception as e:
    print("An unexpected error occurred:", e)
    
    '''This is a more general except block that catches any other exception (error) that might occur during 
    the code execution besides FileNotFoundError.
The as e part assigns the raised exception object to the variable e.
The error message prints a generic message indicating that an unexpected error occurred, 
followed by the details of the exception stored in e. This can be helpful for debugging purposes.'''
