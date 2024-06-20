'''. Write a function in python to count the number of lines from a text file "story.txt" 
which is not starting with an alphabet "T".  
Example: If the file "story.txt" contains the following lines: A boy is playing there. 
There is a playground. 
An aeroplane is in the sky. 
The sky is pink. 
Alphabets and numbers are allowed in the password. 
The function should display the output as 3  '''

def create_story_file():
    content = """A boy is playing there.
There is a playground.
An aeroplane is in the sky.
The sky is pink.
Alphabets and numbers are allowed in the password."""
    
    with open('story.txt', 'w') as file:
        file.write(content)

def count_lines_not_starting_with_T():
    count = 0
    with open('story.txt', 'r') as file:
        lines = file.readlines()  # Read all lines into a list
        for line in lines:
            if not line.lstrip().startswith('T'):  # Using lstrip() to remove leading whitespaces
                count += 1
                
                '''for line in lines::: This line starts a for loop that iterates over each line in the lines list.
if not line.lstrip().startswith('T')::: This line checks if the current line, after stripping leading whitespaces with lstrip(), does not start with the letter 'T'. The startswith() method returns True if the string starts with the specified prefix; otherwise, it returns False.
count += 1: If the condition is met (the line does not start with 'T'), this line increments the count variable by 1.'''
    return count

# Create the story.txt file
create_story_file()

# Call the function and print the result
number_of_lines = count_lines_not_starting_with_T()
print("Number of lines not starting with 'T':", number_of_lines)
