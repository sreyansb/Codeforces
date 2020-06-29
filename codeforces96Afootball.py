one="1111111"
zero="0000000"
t=input()
flag=1
for i in range(len(t)-6):
    
    if t[i:i+7]==one or t[i:i+7]==zero:
        print("YES")
        flag=0
        break
if flag==1:
    print("NO")
        
    
    
