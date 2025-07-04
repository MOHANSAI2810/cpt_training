
try:
    with open('file.txt', 'r') as file:
        str = file.readline()  # Read one line from the file
        print(str)
    a = int(input("Enter the numerator: "))  
    b = int(input("Enter the denominator: ")) 
    div = a / b
    print(f"The result of division is: {div}")

except ZeroDivisionError:
    print("Error: Division by zero is not possible.")
except ValueError:
    print("Error: Please enter valid integers for both the numerator and denominator.")
except KeyboardInterrupt:
    print("Enter the number only")
except FileNotFoundError:
    print("no such file exists")

