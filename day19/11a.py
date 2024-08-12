def is_palindrome(word):
    
    return word == word[::-1]

def count_palindromes(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()  
        words = text.split()  
        palindromes = 0  
        for word in words:
            if is_palindrome(word):
                palindromes += 1
        return palindromes  


filename = "example.txt"
result = count_palindromes(filename)
print("The number of palindromes in the file is: " + str(result))
