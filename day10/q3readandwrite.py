def create_story_file():
    content = """A boy is playing there.
There is a playground.
An aeroplane is in the sky.
The sky is pink.
Alphabets and numbers are allowed in the password."""
    with open("story.txt", "w") as story:
        story.write(content)

def count_lines_not_starting_with_T():
    count = 0
    with open("story.txt", "r") as story:
        lines = story.readlines()
        for line in lines:
            if not line.strip().upper().startswith('T'):
                count += 1
    return count

# Create and write to the file
create_story_file()

# Call the function and print the result
number_of_lines = count_lines_not_starting_with_T()
print("Number of lines not starting with 'T':", number_of_lines)
