# cook your dish here
for i in range(int(input())):
    x,y=map(int,input().split())
    if x*5>=y:
        print("yes")
    else:
        print("NO")