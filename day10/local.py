'''Write a function that counts the number of words in a file named story.txt 
and updates a global variable total_words. Use exception handling to manage any 
errors that occur during file operations (e.g., file not found). Define a local variable within the function to count the words.
'''

total_words = 0

def count_words_in_file():
    global total_words
    try:
        with open("story.txt", "r") as file:
            lines = file.readlines()
            local_word_count = 0
            for line in lines:
                words = line.split()
                local_word_count += len(words)
            total_words = local_word_count
    except FileNotFoundError:
        print("The file 'story.txt' does not exist.")
    except Exception as e:
        print("An error occurred:", e)

# Count the number of words in story.txt
count_words_in_file()
print("Total number of words in 'story.txt':", total_words)
