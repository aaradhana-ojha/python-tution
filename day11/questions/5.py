'''Write a function in Python to count words in a text file those are ending with alphabet 
"e".  '''
def count_words_ending_with_e(filename):
    count = 0

    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.endswith('e'):
                    count += 1

    print("The number of words ending with 'e' is", count)

# Use the function
count_words_ending_with_e('article.txt')


