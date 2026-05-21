n=int(input("Enter The Number...."))
p=0
q=1
if(n==0):
    print(p)
elif(n==1):
    print(q)
elif(1<n):
    for i in range(2,n+1):
     fib=p+q
     p=q
     q=fib
print(fib)