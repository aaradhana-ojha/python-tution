def Book():
    
    with open("Bookname.txt", "w") as f:
        f.write("The names of the following books:\n"
                "One Hundred Years of Solitude\n"
                "The Diary of a Young Girl\n"
                "On the Road\n"
                "After execution, the output will be:\n"
                "One Hundred Years of Solitude\n"
                "The Diary of a Young Girl")

    
    with open("Bookname.txt", "r") as f:
        lines = f.readlines()

    
    for line in lines:
        if 'y' in line.lower():  
            print(line.strip())  


Book()


