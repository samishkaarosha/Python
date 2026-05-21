n=int(input("Enter The Number...."))
c=len(str(abs(n)))
sum=0
for i in range(0,c):
    sum=sum+ int(str(n)[i])
print(sum)