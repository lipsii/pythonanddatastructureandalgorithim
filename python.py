n=int(input())
i=1
while i<=n:
    j=1
    while j<=2*n+1:
        if i==j or j==n+1 or j==2*n+2-i:
            print('*',end="")
        else:
            print(0,end="")
        j=j+1
    i=i+1
    print()
