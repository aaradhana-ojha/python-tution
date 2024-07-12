def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print("Content written to", filename)

def count_lines_starting_with_i(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if line.strip().lower().startswith('i'):
                count += 1
    print("Total number of lines starting with 'i':", count)

write_to_file("data.txt", """The quick brown fox jumps over the lazy dog.
An apple a day keeps the doctor away.
This is a line with 'i' in it.
I am another line starting with 'I'.
Interestingly, this also starts with an 'i'.
A quick movement of the enemy will jeopardize six gunboats.
In the end, it doesn't even matter.
""")


count_lines_starting_with_i("data.txt")
