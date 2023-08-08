# cook your dish here
for _ in range(int(input())):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    count=0
    for i in range(n):
        if a[i]<=9 or a[i]>=80:
            count+-1
    left=n-count
    if count%d==0:
        sol_a=count//d
    else:
        sol_a=count//d+1 
    if left%d==0:
        sol_b=left//d
    else:
        sol_b=left//d+1 
    print(sol_a + sol_b)
    
        



    
    
    

