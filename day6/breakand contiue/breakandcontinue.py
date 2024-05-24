for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    if i == 7:
        break  # Stop the loop when the number is 7
    print(i)
    
'''Explanation
Loop Iteration: The loop iterates over the range from 0 to 9.
Continue Statement:
The if i % 2 == 0: condition checks if the number is even.
If the number is even, the continue statement is executed, 
which skips the rest of the loop body and moves to the next iteration.
Break Statement:
The if i == 7: condition checks if the number is 7.
If the number is 7, the break statement is executed, which exits the loop immediately.'''


'''Detailed Step-by-Step Execution
Iteration 1: i = 0
i % 2 == 0 is True (0 is even), so continue is executed, skipping the print statement.
Iteration 2: i = 1
i % 2 == 0 is False (1 is odd), so it proceeds.
i == 7 is False, so it prints 1.
Iteration 3: i = 2
i % 2 == 0 is True (2 is even), so continue is executed, skipping the print statement.
Iteration 4: i = 3
i % 2 == 0 is False (3 is odd), so it proceeds.
i == 7 is False, so it prints 3.
Iteration 5: i = 4
i % 2 == 0 is True (4 is even), so continue is executed, skipping the print statement.
Iteration 6: i = 5
i % 2 == 0 is False (5 is odd), so it proceeds.
i == 7 is False, so it prints 5.
Iteration 7: i = 6
i % 2 == 0 is True (6 is even), so continue is executed, skipping the print statement.
Iteration 8: i = 7
i % 2 == 0 is False (7 is odd), so it proceeds.
i == 7 is True, so break is executed, exiting the loop.'''