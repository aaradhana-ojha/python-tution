def create_story_file():
    content = """A boy is playing there.
There is a playground.
An aeroplane is in the sky.
The sky is pink.
Alphabets and numbers are allowed in the password."""
    
    with open('story.txt', 'w') as file:
        file.write(content)

def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

# Create the story.txt file
create_story_file()

# Count and print the total number of words
print("Total number of words:", count_words('story.txt'))
