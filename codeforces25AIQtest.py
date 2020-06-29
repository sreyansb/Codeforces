input()
l=input().split()
l=list(map(lambda x:int(x)%2,l))
if l.count(1)>l.count(0):
    print(l.index(0)+1)
else:
    print(l.index(1)+1)
