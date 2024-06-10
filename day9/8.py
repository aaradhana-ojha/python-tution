''' Write a program that display following output: 
SHIFT 
HIFTS 
IFTSH 
FTSHI 
TSHIF 
SHIFT'''
# Define the input string
input_string = "SHIFT"

# Loop to print the rotated versions
for i in range(5):
    rotated_string = input_string[i:] + input_string[:i]
    print(rotated_string)

# Print the original string at the end
print(input_string)

'''Let's go through each iteration of the loop for the string "SHIFT":

First Iteration (i = 0)

input_string[0:] is "SHIFT" (the entire string from index 0 to the end).
input_string[:0] is "" (an empty string because it slices from the start up to index 0).
rotated_string = "SHIFT" + "" = "SHIFT".
Output: SHIFT.
Second Iteration (i = 1)

input_string[1:] is "HIFT" (from index 1 to the end).
input_string[:1] is "S" (from the start up to index 1).
rotated_string = "HIFT" + "S" = "HIFTS".
Output: HIFTS.
Third Iteration (i = 2)

input_string[2:] is "IFT" (from index 2 to the end).
input_string[:2] is "SH" (from the start up to index 2).
rotated_string = "IFT" + "SH" = "IFTSH".
Output: IFTSH.
Fourth Iteration (i = 3)

input_string[3:] is "FT" (from index 3 to the end).
input_string[:3] is "SHI" (from the start up to index 3).
rotated_string = "FT" + "SHI" = "FTSHI".
Output: FTSHI.
Fifth Iteration (i = 4)

input_string[4:] is "T" (from index 4 to the end).
input_string[:4] is "SHIF" (from the start up to index 4).
rotated_string = "T" + "SHIF" = "TSHIF".
Output: TSHIF.'''
