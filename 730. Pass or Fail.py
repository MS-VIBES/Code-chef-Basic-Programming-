t = int(input())
for i in range(t):
    x, y, z= map(int, input().split())
    n = y * 3 - (x - y)
    if n >= z:
        print("PASS")
    else:
        print("FAIL")       # cook your dish here
