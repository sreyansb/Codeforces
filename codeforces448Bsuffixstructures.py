def makingsubsets(s,t):
    pointer=0
    for i in s:
        if t[pointer]==i:
            pointer+=1
        if pointer==len(t):
            break
    return len(t)==pointer
s=input()
t=input()
sa=sorted(s)
ta=sorted(t)
if (sa==ta):
    print("array")
elif makingsubsets(s,t):
    print("automaton")
elif makingsubsets(sa,ta):
    print("both")
else:
    print("need tree")
        
    
        
    
        
            
        
        
            
        
        
        
    
