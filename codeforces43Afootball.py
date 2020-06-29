d={}
for i in range(int(input())):
    k=input()
    if k not in d:
        d[k]=1
    else:
        d[k]+=1
print(sorted(d,key=lambda i:d[i])[-1])
