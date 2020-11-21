n = int(input('Enter desired no. : '))
count=0
x = 2
while True:
    y=True
    for i in range(2,x//2+1):
        if x%i ==0:
            y=False
            break
    if y==True:
        print(x)
        count=count+1
    if count==n:
        break
    x=x+1
        
