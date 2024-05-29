import statistics

data = [1, 2, 3, 4, 5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.mode(data))
'''import statistics: This line imports the statistics module, 
which provides functions for statistical calculations such as mean, median, and mode.

data = [1, 2, 3, 4, 5]: This line creates a list named data 
containing integer values [1, 2, 3, 4, 5]. This list will be 
used as sample data for statistical calculations.

print(statistics.mean(data)): This line calculates the mean 
(average) of the data using the mean() function from the statistics 
module and prints the result. The mean is calculated by adding up 
all the numbers in the dataset and dividing the sum by the total 
number of values. For the given data [1, 2, 3, 4, 5], the mean is (1 + 2 + 3 + 4 + 5) / 5 = 3.

print(statistics.median(data)): This line calculates the median of 
the data using the median() function from the statistics module and 
prints the result. The median is the middle value of a dataset when 
it is sorted in ascending order. If the dataset has an odd number of 
values, the median is the middle value. If the dataset has an even 
number of values, the median is the average of the two middle values. 
For the given data [1, 2, 3, 4, 5], the median is 3.

print(statistics.mode(data)): This line calculates the mode of the 
data using the mode() function from the statistics module and prints 
the result. The mode is the value that appears most frequently in the 
dataset. If there are multiple modes (i.e., multiple values with the 
same highest frequency), the mode function returns one of the modes 
arbitrarily. For the given data [1, 2, 3, 4, 5], there is no mode 
because all values occur only once.'''