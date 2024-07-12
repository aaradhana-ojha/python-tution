'''Write a user defined function counth() in python that displays the number of lines starting with “H” in the file para.txt.'''
def counth():
    
    file = open("para.txt", "r")
    lines = file.readlines()
    count = 0
    
   
    for i in lines:
      
        if  i[0] == 'H':
            count += 1
    

    file.close()
    

    print("The number of lines starting with 'H' is: ",count)


counth()
