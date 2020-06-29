import math
for i in range(int(input())):
    s=input()
    #important to give last condition such that the characters between R
    # and C are only numbers.
    if 'R' in s and 'C' in s and s.index('C')-s.index('R')>1 and s[s.index("R")+1:s.index("C")].isdigit():
        r=s[s.index("R")+1:s.index("C")]
        c=int(s[s.index("C")+1:])
        newstr=""
        while(c>0):
            if c%26==0:
                newstr+=chr(90)
                c=int(math.floor(c/26))
                c-=1
            else:
                newstr+=chr(c%26+64)
                c=int(math.floor(c/26))
        newstr=newstr[::-1]+r
        print(newstr)
    else:
        newnum=0
        newstr=""
        for i in range(len(s)):
            if ord(s[i])>47 and ord(s[i])<58:
                newstr=s[i:]
                newnum=s[:i]
                break
        finum=0
        for j in range(len(newnum)):
            finum+=(26**(j))*(ord(s[len(newnum)-1-j])-64)
            
        fstr="R"+newstr+"C"+str(finum)
        print(fstr)
    
            
        
            
            
        
