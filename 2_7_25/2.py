import csv
with open('people.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    for i in range(2):
        name=input("Enter the name")
        age=int(input("Enter the age"))
        writer.writerow([name,age])
print("Successful")