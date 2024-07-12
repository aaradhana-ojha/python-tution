'''What possible output(s) are expected to be displayed at the screen at the time of execution of the program from the following code? Also specify the minimum and maximum values assigned to day_num variable.'''
import random as r
week_day = {1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat', 7: 'Sun'}
day_num = r.randint(5, 7)
for var in range(1, day_num):
    print(week_day[var], end = ' | ')

'''Mon | Tue | Wed | Thu | Fri |
Mon | Tue | Wed | Thu | Fri | Sat |
Mon | Tue | Wed | Thu | Fri | Sat | Sun |
Minimum value of day_num: 5
Maximum value of day_num: 7'''