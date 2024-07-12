'''Write a program to know the cursor position and print the text from a file “merge.txt” , according to below given specifications:
Print the initial position
Move the cursor to 4th position
Display next 5 character
Move the cursor to the next 10 characters
Print the current position
Print next 10 characters from the current cursur position'''

def cursor_operations():
    file= open("merge.txt", "r")
    initial_position = file.tell()
    print("Initial position: ", initial_position)
    file.seek(3)
    next_5_chars = file.read(5)
    print("Next 5 characters: ", next_5_chars)
    file.seek(file.tell()+10)
    current_position = file.tell()
    print("Current position: ", current_position)
    next_10_chars = file.read(10)
    print("Next 10 characters from the current cursor position: ", next_10_chars)
    file.close()
cursor_operations()