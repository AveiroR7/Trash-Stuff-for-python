n = int(input('Enter desired no. : '))
x = 2
while x <=n:
    y=True
    for i in range(2,x//2+1):
        if x%i ==0:
            y=False
            break
    if y ==True:
        print(x)
    x=x+1
