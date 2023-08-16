# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=0
    y=0
    for i in range(n):
        if a[i]>b[i]:
            x+=a[i]-b[i]
        else:
            y+=b[i]-a[i]
    if x==y:
        print(x)
    else:
        print(-1)