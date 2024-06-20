def count_words_ending_with_e(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        count = sum(1 for word in words if word.endswith('e'))
        return count

# Example usage
print("Words ending with 'e':", count_words_ending_with_e('article.txt'))
