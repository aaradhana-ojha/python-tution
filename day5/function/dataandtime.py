import datetime

def print_current_datetime():
    now = datetime.datetime.now()
    print("Current date and time:", now)
    
'''This function imports the datetime module to get the current date and time.
The function print_current_datetime doesn't take any parameters.
Inside the function, datetime.datetime.now() gets the current date and time.
The function prints the current date and time.'''
# Calling the function
print_current_datetime()

# Output:
# Current date and time: 2024-05-17 12:34:56.789123 (example output, actual output will vary)
