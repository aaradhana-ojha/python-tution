def display_short_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        short_words = [word for word in words if len(word) < 4]
        return short_words

# Example usage
print("Words less than 4 characters:", display_short_words('story.txt'))
