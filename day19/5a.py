def count_total_words(filename):
    total_words = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            total_words += len(words)
    return total_words

# Example usage:
filename = 'data.txt'  # Replace with your file path
total_words = count_total_words(filename)
print("Total number of words in '{}': {}".format(filename, total_words))
