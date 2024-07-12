def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print("Content written to", filename)

def count_digits(filename):
    digit_count = 0
    with open(filename, 'r') as file:
        content = file.read()
        for char in content:
            if char.isdigit():
                digit_count += 1
    print("Total number of digits:", digit_count)


write_to_file("data.txt", "The quick brown fox jumps over the lazy dog. 12345\nAn apple a day keeps the doctor away. 67890")


count_digits("data.txt")
