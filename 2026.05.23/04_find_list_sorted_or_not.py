x=input("Enter your list....").split( )
n=int(x[0])
y=len(x)
z=1
for i in range (1,y):
    if int(x[i])>=n:
        n=int(x[i])
        z=z
    else:
        z=z*0
if z==1:
    print("True")
else:
    print("False")