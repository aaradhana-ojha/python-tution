'''Write a function in Python to count uppercase character and lower character in a text file'''
def count_uppercase_and_lowercase_characters(filename):
    uppercase_count = 0
    lowercase_count = 0

    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char.isupper():
                    uppercase_count += 1
                elif char.islower():
                    lowercase_count += 1

    print("The number of uppercase characters is", uppercase_count)
    print("The number of lowercase characters is", lowercase_count)

# Use the function
count_uppercase_and_lowercase_characters('article.txt')
