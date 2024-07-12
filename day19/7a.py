def count_words_starting_with_a(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.startswith('a') or word.startswith('A'):
                    count += 1  
    return count


filename = 'data.txt'  
count_a_words = count_words_starting_with_a(filename)
print("Number of words starting with 'a' or 'A' in '", filename, "': ", count_a_words)
