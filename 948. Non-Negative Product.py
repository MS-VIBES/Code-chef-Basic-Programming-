# cook your dish here
neg=int(input())
for i in range (neg):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    p=1
    for i in l:
        p=p*i
    if p>=0:
        print("0")
    else:
        print("1")