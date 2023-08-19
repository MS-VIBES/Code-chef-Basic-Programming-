# cook your dish here
t = int(input())
for i in range(t):
    x,y,xr,yr,d = map(int,input().split())
    p = x//xr
    k = y//yr
    h = min(p,k)
    if h>=d:
        print("yes")
    else:
        print("no")