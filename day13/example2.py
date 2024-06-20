import csv

# Data to be written to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Open the CSV file for writing
with open('example2.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object with a tab delimiter
    writer = csv.writer(csvfile, delimiter='\t')
    
    # Write each row of data to the file
    writer.writerows(data)

# Open the CSV file for reading
with open('example2.csv', 'r') as csvfile:
    # Create a CSV reader object with a tab delimiter
    reader = csv.reader(csvfile, delimiter='\t')
    
    # Iterate over each row in the reader object
    for row in reader:
        # Print each row
        print(row)
