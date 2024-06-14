'''. Write a function in Python to read lines from a text file "notes.txt". Your function 
should find and display the occurrence of the word "the"'''

# def count_the_occurrences(filename):
#     the_count = 0
#     try:
#         with open(filename, 'r') as file:
#             for line in file:
#                 words = line.split()
#                 the_count += words.count('the')
#         print("The word 'the' occurs", the_count, "times in the file.")
#     except FileNotFoundError:
#         print("The file", filename, "does not exist.")
#     except Exception as e:
#         print("An error occurred:", str(e))


# count_the_occurrences('notes.txt')

def occur():
    count = 0
    with open("notes.txt", "w") as file:
        file.write("Hello world, the quick brown fox jumps over the lazy dog.")
    
    with open("notes.txt", "r") as oc:
        for line in oc:
            words = line.split()
            count += words.count("the")
    
    print("The word 'the' occurs", count, "times in the file.")

occur()



