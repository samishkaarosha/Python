n=int(input("Enter the number of rows....."))
x=1
i=1
while(i<=n):
    if(i%2>0):
       print("  "*(n-i),"* "*x)
       x=x+2
       i=i+1
    else:
       print("  "*(n-i),"$ "*x)
       x=x+2
       i=i+1