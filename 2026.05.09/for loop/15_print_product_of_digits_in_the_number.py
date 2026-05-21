n=int(input("Enter the number...."))
c=len(str(abs(n)))
x=1
for i in range(0,c):
    x=x* int(str(n)[i])
print(x)