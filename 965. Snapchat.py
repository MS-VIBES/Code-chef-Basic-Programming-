# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    st=0;maxst=0
    for i in range(n):
        if a[i]!=0 and b[i]!=0:
            st+=1;
        elif a[i]==0 or b[i]==0:
            maxst=max(maxst,st)
            st=0
    maxst=max(maxst,st)
    print(maxst)