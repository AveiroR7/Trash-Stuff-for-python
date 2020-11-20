### to check given no. is prime or not ###
n = int(input('Enter no. of rows: '))
if n <= 1:
    print('Number is not Prime')
else:
    for i in range(2,n):
        if n%i == 0:
            print("Number is not Prime Number")
            break
    else:
        print("It is prime Number")
