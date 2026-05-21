n=int(input("Enter The Number"))
c=len(str(abs(n)))
sum=0
i=0
while(i<c):
    sum=sum+ int(str(n)[i])
    i=i+1
print(sum)