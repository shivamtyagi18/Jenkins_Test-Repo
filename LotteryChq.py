import math
import sys

#t= int(input())
t=int(sys.argv[1])
print(t)
for k in range(1, t + 1):
    #N=int(input())
    N=int(sys.argv[2])
    a=[]
    b=[]
    while N>=1:
        a.append(math.floor(N%10))
        N=N/10
        
    a=(a[::-1])
    print(a)
    
    for i in range(len(a)):
        if a[i]==4:
            a[i]=2
            b.append(2)
        else:
            b.append(0)
    
    print(a,b)
    
    num1=''.join(map(str,a))
    num2=''.join(map(str,b))
            
    
    
    
    print("Case #{}: {} {} ".format(k,num1,num2))
