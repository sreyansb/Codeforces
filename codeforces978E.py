n,w=map(int,input().split())
a=list(map(int,input().split()))
sumtillnow=0
maxi=0
mini=0
for i in a:
    sumtillnow+=i
    maxi=max(maxi,sumtillnow)
    mini=min(mini,sumtillnow)
print(max(w-maxi+mini+1,0))
