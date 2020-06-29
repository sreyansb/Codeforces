input()
t=input()
while(True):
    if '10' not in t and '01' not in t :
        break
    else:
        if '10' in t:
            t=t.replace('10','')
        elif '01' in t:
            t=t.replace('01','')
print(len(t))
    
