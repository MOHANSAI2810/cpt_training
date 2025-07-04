def hello(i,j):
    try:
        while True:
            i+=1
            if i>j:
                raise StopIteration
            print(i)
    except:
        print("These are the first 20 numbers")
i=int(input("Enter the first value to start"))
j=int(input("Enter the second value to stop"))
hello(i,j)