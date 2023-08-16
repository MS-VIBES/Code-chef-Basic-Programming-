# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=107/100
    if a*x>=y:
        print("YES")
    else:
        print("No")