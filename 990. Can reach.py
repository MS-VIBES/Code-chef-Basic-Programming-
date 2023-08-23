for _ in range(int(input())):
    x,y,k=map(int,input().split())
    print("NO") if(abs(x)%k!=0 or abs(y)%k!=0) else print("YES")