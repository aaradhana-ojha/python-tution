def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        print("Total number of lines:", line_count)


count_lines('data.txt')
