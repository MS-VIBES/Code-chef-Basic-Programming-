# cook your dish here
t=int(input())
for _ in range(t):
    lst=list(map(int,input().split()))
    monopoly=max(lst)
    lst.remove(monopoly)
    b=sum(lst)
    if (monopoly>b):
        print("YES")
    else:
        print("NO")