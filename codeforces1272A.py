for _ in range(int(input())):
    a,b,c=map(int,input().split())
    mini=abs(a-b)+abs(b-c)+abs(c-a)
    for  i in range(a-1,a+2):
        for j in range(b-1,b+2):
            for k in range(c-1,c+2):
                mini=min(mini,abs(i-j)+abs(j-k)+abs(i-k))
    print(int(mini))
            
        
