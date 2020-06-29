n=input()
s=""
if n[0]=='9':
    s+='9'
else:
    s=s+str(min(int(n[0]),9-int(n[0])))
for i in n[1:]:
    s=s+str(min(int(i),9-int(i)))
print(s)
    
