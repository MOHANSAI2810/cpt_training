import csv
with open('people.csv','r') as file:
    reader=csv.reader(file)
    for i in reader:
        print(i)