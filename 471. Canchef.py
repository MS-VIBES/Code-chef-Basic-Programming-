# cook your dish here
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    total_distance = 2 * Y
    max_distance = X * 15
    if max_distance >= total_distance:
        print("YES")
    else:
        print("NO")