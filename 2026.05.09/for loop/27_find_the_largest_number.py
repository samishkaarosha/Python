n=input("Enter the number list.....").split(" ")
m=[int(y) for y in n]
max=0
x=len(n)
for i in range (0,x):
    if(max<m[i]):
        max=m[i]
    else:
        max=max
print("The largest number is",max)
