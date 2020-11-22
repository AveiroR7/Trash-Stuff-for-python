str = input('Enter the String : ')
i = 0
for x in str:
    print('The character present at index : {} and Negative Index : {} is : {} '.format(i,i-len(str),x))
    i=i+1
