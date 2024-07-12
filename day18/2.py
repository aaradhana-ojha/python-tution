'''Write a function displaywords() in python to read lines from a text file poem.txt and display those words which are less than or equal to 4 characters.'''

def displaywords():
    
    file = open("poem.txt", "r")
    lines = file.readlines()
    
    
   
    for line in lines:
      
        words=line.split()
        
        for word in words:
            if len(word)<=4:
                print(word)
    

    file.close()
    

displaywords()
