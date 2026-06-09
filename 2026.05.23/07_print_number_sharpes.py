n=int(input("Enter the number of rows...."))
m=len(str(abs(n)))
for i in range(0,n):
    x=int(((n-i))*(m+1))
    print(" "*x,end="")
    for j in range(1,i+2):
        c=len(str(abs(j)))
        print(j,end=" "*(m+1-c))
    for k in range(1,i+1):
        c=len(str(abs(k-i)))
        print(i+1-k,end=" "*(m+1-c))
    
    print( )

         