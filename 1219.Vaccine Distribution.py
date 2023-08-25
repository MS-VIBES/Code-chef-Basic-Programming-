# cook your dish here
t=int(input()) 
for i in range(t): 
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        if a[i]<=9 or a[i]>=80:
            c +=1
    g=n-c
    if c%d==0:
        d1=c//d
    else:
        d1=c//d+1
    if g%d==0:
        d2=g//d
    else:
        d2=g//d+1    
    print(d1+d2)    
    

