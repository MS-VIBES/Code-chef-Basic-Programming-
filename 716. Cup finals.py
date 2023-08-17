# cook your dish here
for i in range(int(input())):
        x,y,d=map(int,input().split())
        print("YES") if (abs(x-y)<=d) else print("NO")