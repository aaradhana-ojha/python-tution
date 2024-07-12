def print_words_up_to_4(filename):
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) <= 4:
                    print(word)


filename = 'data.txt' 
print("Words up to 4 characters in length:")
print_words_up_to_4(filename)
