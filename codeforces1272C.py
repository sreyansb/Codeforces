n,k=map(int,input().split())
s=input()
valid=list(input().split())
for i in valid:
    s=s.replace(i,'1')
lastpositionofzero=n
nos=0
for i in range(n-1,-1,-1):
    if s[i]!='1':
        lastpositionofzero=i
    else:
        nos+=lastpositionofzero-i
    #print(nos)
print(nos)
        
        
        
    
