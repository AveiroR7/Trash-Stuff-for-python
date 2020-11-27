#WAP to reverse content of the given string by using while loop.

s=input("Enter the String: ")
output=''
i=len(s)-1
while i>=0:
    output=output+s[i]
    i=i-1
print(output)
