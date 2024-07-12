import csv
#This line imports the csv module, which provides functionality to read from and write to CSV files in Python.
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago'],
    ['Charlie', 35, 'Chicago'],
    ['Charlie', 35, 'Chicago'],
]


with open('example.csv', 'w', newline='') as csvfile:
    
    writer = csv.writer(csvfile)
   
    writer.writerows(data)
