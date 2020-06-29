n=int(input())
#li has to be a list of characters/strigs
li=input().split()
li="".join(li)

k=li.count('1')
if k==1 or k==len(li):
    print(1)
elif k==0:
    print(0)
else:
    nof=1
    if '1' in li:
        end=li.rindex('1')
    else:
        li=""
    while(li):
        li=li[:end]
        if '1' in li:
            nof*=end-li.rindex('1')
            end=li.rindex('1')
        else:
            li=""
    print(nof)
    
    
