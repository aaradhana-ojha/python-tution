try:
    # Code that may raise an exception
    file = open('file.txt', 'r')  # Attempt to open the file
    content = file.read()         # Attempt to read from the file
    file.close()                  # Close the file
    print(content)                # Print the file content
except FileNotFoundError:
    # Handle the specific exception when the file is not found
    print('File not found')
except Exception as e:
    # Handle any other exceptions
    print('An error occurred:', e)
    
    
'''The try block contains the code that you want to execute. 
In this case, it tries to open the file, read its content, and then close it.
If an exception occurs within the try block (for example, if the file is not found), 
Python immediately jumps to the corresponding except block.
If the exception matches the type specified after except, the code within 
that except block is executed. In this example, FileNotFoundError is caught 
separately from other exceptions.
If the exception does not match any of the specified types, it will be caught 
by the general except block. You can use except Exception as e to catch all 
types of exceptions and print out the specific error message (e contains the error object).
After executing the appropriate except block, the program continues to run normally.'''
