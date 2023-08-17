# cook your dish here
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    after_discount=n-(0.1*n)
    if after_discount<m:
        print("ONLINE")
    elif after_discount>m:
        print("DINING")
    else:
        print("EITHER")