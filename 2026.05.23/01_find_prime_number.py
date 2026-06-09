n=int(input("Enter the number...."))
x=1
for i in range(2,n-1):
    x=x*(n%i)
if x==0:
    print(n,"is not prime number")
else:
    print(n,"is prime number")