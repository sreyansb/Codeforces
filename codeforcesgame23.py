s=input().split()
n=int(s[0])
m=int(s[1])
flag=0
no=0
k=1
if n==m:
    print("0")
    flag=1
elif n<m:
    k=m/n
    while(k>1):#important condition:otherwise loop will go on infinitely
        if k%6==0:
            k/=6
            no+=2
        elif k%3==0:
            k/=3
            no+=1
        elif k%2==0:
            k/=2
            no+=1
        else:
            break
        #print(k)
else:
    print("-1")
    flag=1
if k==1 and flag==0:
    print(no)
elif k!=1 and flag==0:
    print(-1)
    
