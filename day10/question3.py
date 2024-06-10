def count_lines_not_starting_with_T():
    count = 0
    with open('story.txt', 'r') as file:
        lines = file.readlines()  # Read all lines into a list
        for line in lines:
            if not line.startswith('T'):
                count += 1
    return count

# Call the function and print the result
number_of_lines = count_lines_not_starting_with_T()
print("Number of lines not starting with 'T':", number_of_lines)



def count_lines_not_starting_with_T():
    count = 0
    with open("story.txt", "r") as story:
        lines = story.readlines()
        for line in lines:
            if not line.strip().upper().startswith('T') and not line.strip().lower().startswith('t'):
                count += 1
    return count

# Call the function and print the result
number_of_lines = count_lines_not_starting_with_T()
print("Number of lines not starting with 'T':", number_of_lines)


def count():
    count = 0
    with open("story.txt") as story:
        lines = story.readlines()
        for line in lines:
            if not line.strip().upper().startswith('T'):
                count += 1
    return count

# Call the function and print the result
print("Number of lines not starting with 'T':", count())
