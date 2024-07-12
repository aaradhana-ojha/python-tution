def count_even_odd_words_each_line(filename):
    line_number = 1
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            even_count = 0
            odd_count = 0
            for word in words:
                if len(word) % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
            print("Line", line_number, ":", even_count, "even-length words,", odd_count, "odd-length words")
            line_number += 1


count_even_odd_words_each_line('data.txt')
