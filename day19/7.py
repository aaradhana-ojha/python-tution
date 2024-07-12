def print_even_lines(filename):
    line_number = 1  
    with open(filename, 'r') as file:
        for line in file:
            if line_number % 2 == 0:  
                print("Line", line_number, ":", line.strip())
            line_number += 1  


print("Even-numbered lines:")
print_even_lines('data.txt')
