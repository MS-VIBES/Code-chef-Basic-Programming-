t=int(input())
while(t>0):
    d,a=map(int,input().split())
    s=0
    for k in range(d):
        s=0
        for j in range(1,a+1,1):
            s+=j
        a=s
    print(s)
    t-=1