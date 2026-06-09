n=int(input("Enter the number....."))
m=len(str(abs(n*n)))
for i in range( 1,n+1):
    for j in range( 1,n+1):
        c=len(str(abs(j*i)))
        print(j*i,end=" "*(m+1-c))
    print( )