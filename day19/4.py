def count_lines_starting_with(filename, symbols):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            line_starts_with_symbol = line.startswith(tuple(symbols))
            if line_starts_with_symbol:
                count += 1
    print("Number of lines starting with symbols", symbols, ":", count)


count_lines_starting_with('data.txt', ['@', '#', '$'])



def count_lines_starting_with(filename, symbols):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if len(line) > 0 and line[0] in symbols:
                count += 1
    print("Number of lines starting with symbols", symbols, ":", count)


count_lines_starting_with('data.txt', ['@', '#', '$'])
