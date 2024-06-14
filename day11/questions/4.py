''' Write a function display_words() in python to read lines from a text file "story.txt", and 
display those words, which are less than 4 characters. '''
def display_words():
    
        with open("story.txt", "r") as file:
            for line in file:
                words = line.split()
                for word in words:
                    if len(word) < 4:
                        print(word)
    


display_words()



