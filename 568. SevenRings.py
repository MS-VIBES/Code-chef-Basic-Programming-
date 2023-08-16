# cook your dish here
t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    total_bill=n*x
    a=len(str(total_bill))
    if a == 5:
        print("YES")
    else:
        print("NO")

   