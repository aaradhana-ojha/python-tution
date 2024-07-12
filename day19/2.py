def count_words_in_each_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        line_number = 1
        for line in lines:
            word_count = len(line.split())
            print("Line", line_number, ":", word_count, "words")
            line_number += 1


count_words_in_each_line('data.txt')
