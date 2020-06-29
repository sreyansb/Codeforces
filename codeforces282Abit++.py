t=int(input())
x=0
for i in range(t):
    k=input()
    if k=="++X" or k=="X++":
        x+=1
    if k=="--X" or k=="X--":
        x-=1
print(x)
    
