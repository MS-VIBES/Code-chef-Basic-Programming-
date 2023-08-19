# cook your dish here
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=set(a)
    ans=list(ans)
    ans.sort()
    print(ans[-1]+ans[-2])