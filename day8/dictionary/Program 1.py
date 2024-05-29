#Count the number of times a character appears in a given string using a dictionary.

def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Example usage
string = "hello world"
print(count_characters(string))
