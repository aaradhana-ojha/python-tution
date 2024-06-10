'''Write a program that reads from a file named input.txt 
and writes its content to a file named output.txt. 
Use exception handling to manage the cases where the 
file input.txt does not exist. Define a global variable 
file_content to store the content read from the file.
'''
# file_content = ""

# def read_file():
#     global file_content
#     try:
#         with open("input.txt", "r") as file:
#             file_content = file.read()
#     except FileNotFoundError:
#         print("The file 'input.txt' does not exist.")
#     except Exception as e:
#         print("An error occurred:", e)

# def write_file():
#     global file_content
#     try:
#         with open("output.txt", "w") as file:
#             file.write(file_content)
#     except Exception as e:
#         print("An error occurred while writing to 'output.txt':", e)


# read_file()
# write_file()


filecontent = ""

def readfile():
    global filecontent
    with open("input.txt", "r") as input:
        filecontent = input.read()
        print(filecontent)

def writefile():
    global filecontent
    with open("output.txt", "w") as output:
        output.write(filecontent)


readfile()
writefile()
