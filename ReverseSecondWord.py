#wap to reverse internal content of every 2nd word present in given string.

s=input('Enter the words:')
l=s.split()
i=0
l1=[]
while i < len(l):
    if i%2 == 0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1
output=' '.join(l1)
print(output)
