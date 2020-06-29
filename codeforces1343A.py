for _ in range(int(input())):
    n=int(input())
    i=4
    x=0
    while(i-1<=n):
        if n%(i-1)==0:
            x=n//(i-1)
            break
        i<<=1
    print(x)
            
