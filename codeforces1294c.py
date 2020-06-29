def findprimefactors(n):
    l=[]
    while(n%2==0):
        l.append(2)
        n//=2
    for i in range(3,int(n**.5)+1,2):
        while(n%i==0):
            n//=i
            l.append(i)
    if n>2:
        l.append(n)
    return l   
     
for _ in range(int(input())):
    n=int(input())
    k=findprimefactors(n)
    l=set(k)
    z=len(l)
    if z>=3:
        print("YES")
        l=list(l)
        prod=l[0]*l[1]
        prod1=1
        print(*l[:2],end=" ")
        for i in k:
            prod1*=i
        print(prod1//prod)
    elif z==2:
        if len(k)<4:
            print("NO")
        else:
            prod=1
            print("YES")
            l=list(l)
            prod1=1
            for i in l:
                print(i,end=" ")
                prod*=i
            for i in k:
                prod1*=i
            print(prod1//prod)
    elif z==1:
        prod=1
        if len(k)>5:
            print("YES")
            print(k[0],k[1]*k[2],end=" ")
            for i in k[3:]:
                prod*=i
            print(prod)
        else:
            print("NO")
    else:
        print("NO")
                
            
        
            
