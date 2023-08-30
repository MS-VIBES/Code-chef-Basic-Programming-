# cook your dish here
t = int(input())
for i in range(t):
    m = list(map(int, input().split()))
    o = list(map(int, input().split()))
    p = list(map(int, input().split()))
    a = sum(m)
    b = sum(o)
    c = sum(p)
    d = sum([m[0], o[0], p[0]])
    e = sum([m[1], o[1], p[1]])
    f = sum([m[2], o[2], p[2]])
    maxi = max(a, b, c, d, e, f)
    if maxi % 2 == 0 and maxi != 0:
        maxi -= 1
    print(maxi)