def count_words_ending_with_a(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.endswith('a') or word.endswith('A'):
                    count += 1  
    return count


filename = 'data.txt'  
count_a_words = count_words_ending_with_a(filename)
print("Number of words ending with 'a' or 'A' in '", filename, "': ", count_a_words)
