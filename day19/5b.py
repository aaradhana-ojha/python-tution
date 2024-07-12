def count_total_words_alpha(filename):
    total_words = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.isalpha():
                    total_words += 1
    print("Total number of alphabetic words in '{}': {}".format(filename, total_words))

# Example usage:
filename = 'data.txt'  # Replace with your file path
count_total_words_alpha(filename)
