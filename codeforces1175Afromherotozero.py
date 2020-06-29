for j in range(int(input())):
    m,n=map(int,input().split())
    nos=0
    while(m>1):
        if m%n==0:
            m/=n
            nos+=1
        else:
            m-=1
            nos+=1
    print(nos+1)
            
        
