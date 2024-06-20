def count_the_occurrences(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        count = sum(1 for word in words if word.lower() == "the")
        return count

# Example usage
print("Occurrence of the word 'the':", count_the_occurrences('notes.txt'))
