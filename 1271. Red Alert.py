# cook your dish here
t=int(input())
for i in range(t):
    n,d,h=map(int,input().split())
    a=list(map(int,input().split()))
    k=0
    for i in range(n):
        if(a[i]>0):
            k=k+a[i]
        elif(a[i]==0):
            k=k-d
            if k<0:
                k=0
        if k>h:
            print('YES')
            break
    else:
        print('NO')
        