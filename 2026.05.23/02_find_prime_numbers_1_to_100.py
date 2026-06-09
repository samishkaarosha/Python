for n in range(1,101):
    x=1
    for i in range(2,n-1):
        x=x*(n%i)
    if x>0:
        print(n,end=",")
    else:
        print(end="")
    