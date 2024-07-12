import csv

def addRecord(TName, Post, subject):
    with open('Teacher.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([TName, Post, subject])

addRecord("Mahendra", "PGT", "Maths")
addRecord("Seema", "TGT", "Hindi")
addRecord("Neha", "PGT", "CS")
addRecord("Rahul", "PGT", "English")
