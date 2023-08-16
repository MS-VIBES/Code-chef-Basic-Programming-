# cook your dish here
for _ in range(int(input())):
    n,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    flag="yes"
    for i in range(n):
        if ((b[i]-a[i]!=x) and (b[i]-a[i]!=y)):
            flag="No"
            break
    print(flag)