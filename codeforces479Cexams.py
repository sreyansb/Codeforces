l=[]
bl=[]
for _ in range(int(input())):
    a,b=map(int,input().split())
    l.append((a,b))
    bl.append(b)
bl.sort()
l=sorted(l,key=lambda x:(x[0],x[1]))
current_answer=0
for i in l:
    if current_answer<=i[1]:
        current_answer=i[1]
    else:
        current_answer=i[0]
print(current_answer)
"""
bk=[x[1] for x in l]
ak=set([x[0] for x in l])
j=len(ak)
if bk==bl:
    if j==1:
        print(min(l[0][0],bk[-1]))
    else:
        print(bk[-1])
elif bk[::-1]==bl and j==1:
    print(min(bk[0],l[-1][0]))
else:
    print(l[-1][0])
"""
               
