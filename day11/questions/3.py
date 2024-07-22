''' Write a function in Python to count the words "this" and "these" present in a text file 
"article.txt". [Note that the words "this" and "these" are complete words'''

def count_this_and_these(filename):
    this_count = 0
    these_count = 0
    
    with open(filename, 'w') as file:
        file.write("The quick brown fox jumps over the lazy dog. It was a bright, sunny day, and the park was filled with people enjoying the weather. Children were playing on the swings, while parents watched them with smiles on their faces. Birds were chirping in the trees, adding to the cheerful atmosphere. In the distance, a group of friends were having a picnic, laughing and chatting as they shared stories and food. The aroma of freshly cut grass filled the air, making everyone feel refreshed and happy. this It was one of those perfect days that you wish could last forever.")

    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            this_count += words.count('this')
            these_count += words.count('these')

    print("The word 'this' occurs", this_count, "times in the file.")
    print("The word 'these' occurs", these_count, "times in the file.")

# Use the function
count_this_and_these('article.txt')
