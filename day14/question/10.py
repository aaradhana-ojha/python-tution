def count_lines_not_starting_with_T(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if not line.lstrip().startswith('T'):
                count += 1
    return count

# Example usage
print("Number of lines not starting with 'T':", count_lines_not_starting_with_T('story.txt'))
