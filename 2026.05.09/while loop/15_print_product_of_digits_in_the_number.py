n=int(input("Enter the number...."))
c=len(str(abs(n)))
x=1
i=0
while(i<c):
    x=x* int(str(n)[i])
    i=i+1
print(x)