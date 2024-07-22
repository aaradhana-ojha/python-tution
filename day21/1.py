'''rite a function in Python that displays the book names having 
y in their name from a text file Bookname.t 3 
  Example : 
  s the names of following books : 
  One Hundred Years of Solitude 
  The Diary of a Young Girl 
  On the Road 
  After execution, the output will be : 
  One Hundred Years of Solitude  
  The Diary of a Young Girl
 OR  
91 Page 10 of 19  
 (b) Write a function RevString() 
prints the words  The rest of the 
content is displayed normally.   3 
  Example : 
  If content in the text file is : 
  UBUNTU IS AN OPEN SOURCE OPERATING SYSTEM 
  Output will be : 
  UBUNTU IS AN NEPO SOURCE GNITAREPO SYSTEM  
   '''
   
def display_books_with_y():
    with open('Bookname.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if 'y' in line or 'Y' in line:
                print(line.strip())


display_books_with_y()
