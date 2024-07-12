def count_and_display_same_letter_start_end(filename):
    same_letter_count = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            if words:  
                first_word = words[0].strip().lower() 
                last_word = words[-1].strip().lower()  
                if first_word and last_word and first_word[0] == last_word[-1]:
                    print(line.strip()) 
                    same_letter_count += 1

    print("Total number of lines starting and ending with the same letter:", same_letter_count)

filename = 'data.txt'  
print("Lines starting and ending with the same letter:")
count_and_display_same_letter_start_end(filename)
