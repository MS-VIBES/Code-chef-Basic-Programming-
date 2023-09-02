# cook your dish here
# cook your dish here
t = int(input())

for tc in range (t):
    n = int(input())
    s = n*(n+1)/2
    F = list(map(int,input().split()))[1:]
    r = int(input())
    for x in F:
        s-=x
    n = (n+1)//2
    res = ((n-r)/n)*s
    print("%.4f"%res)
    