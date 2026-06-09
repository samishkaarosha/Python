x=input("Enter your list....").split( )
n=int(input("Enter what the number are you find...."))
y=len(x)
z=1
for i in range (0,y):
    if int(x[i])==n:
        z=z*0
    else:
        z=z
if z==0:
    print("True")
else:
    print("False")