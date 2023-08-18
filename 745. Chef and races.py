# cook your dish here
for i in range(int(input())):
        x,y,a,b=map(int,input().split())
        if len(set([x,y,a,b]))==len([x,y,a,b]):
                print(2)
        elif len(set([x,y,a,b]))==3:
                print(1)
        else:
                print(0)