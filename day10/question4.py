'''3. Write a function in Python to count and display the total number of words in a text 
file. '''

def create_story_file():
    content = """A boy is playing there.
There is a playground.
An aeroplane is in the sky.
The sky is pink.
Alphabets and numbers are allowed in the password."""
    
    with open('story.txt', 'w') as file:
        file.write(content)

def count_lines_starting_with_T_or_t():
    count = 0
    with open('story.txt', 'r') as file:
        lines = file.readlines()  # Read all lines into a list
        for line in lines:
            if line.lstrip().startswith(('T', 't')):  # Check if line starts with 'T' or 't'
                count += 1
    return count

# Create the story.txt file
create_story_file()

# Call the function and print the result
number_of_lines = count_lines_starting_with_T_or_t()
print("Number of lines starting with 'T' or 't':", number_of_lines)
