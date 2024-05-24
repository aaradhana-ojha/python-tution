'''The continue statement skips the 
rest of the code inside the loop for 
the current iteration and jumps to the next iteration.'''

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Output: 1 3 5 7 9
