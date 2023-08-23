# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    for i in range(2):
        if(a>=b):
            b+=c
            c=d
        else:
            a+=c
            c=d
    if(a>=b):
        print('N')
    else:print('S')