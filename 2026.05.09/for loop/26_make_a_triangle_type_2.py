n=int(input("Enter the number of rows....."))
x=1
for i in range(1,n+1):
    if(i%2>0):
       print("  "*(n-i),"* "*x)
       x=x+2
    else:
       print("  "*(n-i),"$ "*x)
       x=x+2