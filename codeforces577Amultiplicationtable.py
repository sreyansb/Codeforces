k=input().split()
n=int(k[0])
x=int(k[1])
no=0
m=n*n
if x==1 or x==m:
    no+=1
else:
    for i in range(1,int(pow(x,0.5))+1):
        if i>n:
            break
        if x%i==0:
            k=x//i
            if k<=n and k!=i:
                no+=2
            elif k<=n and k==i:
                no+=1
print(no)
            
