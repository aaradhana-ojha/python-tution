def count_lines_ending_with(filename, symbols):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if line.strip().endswith(tuple(symbols)):
                count += 1
    print("Number of lines ending with symbols", symbols, ":", count)

count_lines_ending_with('data.txt', ['.', '?', '!'])



def count_lines_ending_with(filename, symbols):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if len(stripped_line) > 0 and stripped_line[-1] in symbols:
                count += 1
    print("Number of lines ending with symbols", symbols, ":", count)


count_lines_ending_with('data.txt', ['.', '?', '!'])

