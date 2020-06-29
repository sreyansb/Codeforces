"""
TWO CASES FOR MAKING ALL THE ARRAY ELEMENTS EQUAL TO ZERO:
1)SUM IS EVEN
2)MAX OF a IS LESS THAN SUM OF THE ARRAY
"""
n=int(input())
a=list(map(int,input().split()))
k=sum(a)
if k%2==1 or 2*max(a)>k:
    print("no")
else:
    print("yes")
    
    
    

