x=input("Enter your list....").split( )
n=int(input("Enter your number...."))
y=len(x)
z=1
for i in range (0,y):
    for j in range(0,y):
        if int(x[i])+int(x[j])==n:
            if i==j:
                print(end="")
            else:
                print(int(x[i]),int(x[j]))
        else:
            print(end="")