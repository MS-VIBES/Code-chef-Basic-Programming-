# cook your dish 
testcase=int(input())
for _ in range(testcase):
    n,x=map(int,input().split())
    half=n/2
    if x>=half:
        print("YES")
    else:
        print("NO")
     
