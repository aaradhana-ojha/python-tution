'''Question:
Write a Python script that attempts to perform the following actions with appropriate exception handling:

Open a file named 'example.txt' in write mode and write the text "Hello, World!" to it.
Open the same file in append mode and add the text " Welcome to Python file handling." to it.
Open the file in read mode and print its content.
Your script should handle the FileNotFoundError and any other exceptions that might occur, printing appropriate error messages.'''


try:
    # Attempt to open the file in write mode and write text to it
    file = open('example.txt', 'w')
    file.write('Hello, World!')
    file.close()

    # Attempt to open the file in append mode and add text to it
    file = open('example.txt', 'a')
    file.write(' Welcome to Python file handling.')
    file.close()

    # Attempt to open the file in read mode and print its content
    file = open('example.txt', 'r')
    content = file.read()
    file.close()
    print(content)
except FileNotFoundError:
    # Handle the specific exception when the file is not found
    print('File not found')
except Exception as e:
    # Handle any other exceptions
    print('An error occurred:', e)
    
    
    
    
try:
    # Open the file in write mode and write text to it
    with open('example.txt', 'w') as file:
        file.write('Hello, World!')

    # Open the file in append mode and add text to it
    with open('example.txt', 'a') as file:
        file.write(' Welcome to Python file handling.')

    # Open the file in read mode and print its content
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    # Handle the specific exception when the file is not found
    print('File not found')
except Exception as e:
    # Handle any other exceptions
    print('An error occurred:', e)

