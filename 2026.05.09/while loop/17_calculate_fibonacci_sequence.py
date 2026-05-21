n=int(input("Enter The Number...."))
p=0
q=1
if(n==0):
    print(p)
elif(n==1):
    print(q)
elif(1<n):
    i=2
    while(i<=n):
     fib=p+q
     p=q
     q=fib
     i=i+1
print(fib)