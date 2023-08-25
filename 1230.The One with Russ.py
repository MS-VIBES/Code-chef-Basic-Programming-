# cook your dish here
for _ in range(int(input())):
    n,x,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    count=0
    for i in range(n):
        if abs(a[i]-b[i])<=k:
            count+=1 
    if count>=x:
        print("YES")
    else:
        print("NO")