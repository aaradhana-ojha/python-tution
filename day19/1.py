def count_lines_with_and(filename):
    count = 0
    word_frequency = 0
    with open(filename, 'r') as file:
        for line in file:
            if 'and' in line:
                count += 1
                word_frequency += line.lower().split().count('and')
    print("Number of lines containing the word 'and':", count)
    print("Frequency of the word 'and':", word_frequency)


count_lines_with_and('data.txt')
