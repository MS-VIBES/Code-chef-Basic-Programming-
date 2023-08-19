# cook your dish here
t=int(input())
for i in range(t):
    f, s, th= map(str, input().split())
    x, y= map(str, input().split())
    if(f in (x,y)):
        print(f)
    elif(s in (x,y)):
        print(s)
    else:
        print(th)