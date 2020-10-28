n=int(input())
while(True):
    k=n
    sumi=0
    while(k):
        sumi+=k%10
        k//=10
    if sumi%4==0:
        print(n)
        break
    n+=1
