try:
    a=int(input("Enter the num"))
    assert (a%2==0), 'even'
    print('even')
except AssertionError:
    print('hi')