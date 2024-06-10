'''Read 7 characters from the end of the file using seek function.
File=(say my name) solve it'''

with open("say_my_name.txt", "w") as file:
    file.write("say my name")


with open("say_my_name.txt", "rb") as file:
    
    file.seek(-7, 2)  

    
    data = file.read().decode()  
    print("Last 7 characters of the file:")
    print(data)
