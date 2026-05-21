n=input("Enter the number list.....").split(" ")
m=[int(y) for y in n]
max=0
x=len(n)
i=0
while(i<x):
    if(max<m[i]):
        max=m[i]
        i=i+1
    else:
        max=max
        i=i+1
print("The largest number is",max)
