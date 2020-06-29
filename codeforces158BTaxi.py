t=int(input())
l=input().split()
l=list(map(int,l))
l=sorted(l)
one=[]
two=[]
three=[]
four=[]
flag=0
for i in l:
    if i==1:
        one.append(1)
    elif i==2:
        two.append(2)
    elif i==3:
        three.append(3)
    else:
        four.append(4)
not1=0
k=0
j=0

if len(one)==len(three):
    not1+=len(one)
    #print(not1)
    one=[]
    three=[]

else:
    not1+=min(len(one),(len(three)))
    #print(not1)
    if len(one)>len(three):
        k=len(one)-len(three)
    else:
        not1+=len(three)-len(one)
        #print(not1)
if len(two)>0:
    if len(two)%2==0:
        not1+=len(two)//2
        if k>0 and k%4==0:
            not1+=(k)//4
        elif k>0 and k%4!=0:
            not1+=((k)//4)+1
    
    elif len(two)%2==1:
        not1+=((len(two)-1)//2)+1
        #print(not1)
        if k>0 and (k-2)%4==0:
            not1+=(abs(k-2))//4
            #print(not1)
        elif k>0 and (k-2)%4!=0 :
            not1+=((abs(k-2))//4)
            if k>2:
                flag=1
            #print(not1)
else:
    if k>0 and k%4==0:
            not1+=(k)//4
    elif k>0 and k%4!=0:
        not1+=((k)//4)+1
    
    


not1+=len(four)
if flag==1:
    print(not1+1)
else:
    print(not1)


    
