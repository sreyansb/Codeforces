n=int(input())
s=input()
di={}
for i in range(n-1):
    k=s[i]+s[i+1]
    if k not in di:
        di[k]=0
    di[k]+=1
di=sorted(di,key=lambda x:di[x],reverse=True)
print(di[0])
