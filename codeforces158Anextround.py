l=input().split()
n=int(l[0])
k=int(l[1])
l=input().split()
l=[int(i) for i in l]
m=[]
fag=0
for i in l:
    if len(m)>=k:
        break
    if i>0:
        m.append(i)
        fag+=1
    else:
        fag=0
        break
if fag>0:
    for i in range(fag,len(l)):
        if l[i]==m[-1]:
            m.append(l[i])
    
print(len(m))
