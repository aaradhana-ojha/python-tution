'''3. Write a function in Python to count and display the total number of words in a text 
file.  '''
def count_words_in_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print("Total number of words:", word_count)


filename = "input.txt"
count_words_in_file(filename)


