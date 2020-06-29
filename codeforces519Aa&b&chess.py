sumw=0
sumb=0
for i in range(8):
    s=input()
    if 'q' in s:
        sumb+=9*s.count('q')
    if 'r' in s:
        sumb+=5*s.count('r')
    if 'b' in s:
        sumb+=3*s.count('b')
    if 'n' in s:
        sumb+=3*s.count('n')
    if 'p' in s:
        sumb+=s.count('p')
        
    if 'Q' in s:
        sumw+=9*s.count('Q')
    if 'R' in s:
        sumw+=5*s.count('R')
    if 'B' in s:
        sumw+=3*s.count('B')
    if 'N' in s:
        sumw+=3*s.count('N')
    if 'P' in s:
        sumw+=s.count('P')
if sumw>sumb:
    print("White")
elif sumw==sumb:
    print("Draw")
else:
    print("Black")
    
