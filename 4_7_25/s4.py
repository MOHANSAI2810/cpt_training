import calendar
a=int(input("Enter the year"))
b=int(input("Enter the month"))
c=calendar.month(a,b)
print(c)
if calendar.isleap(a):
    print("Leap year")
else:
    print("not leap year")