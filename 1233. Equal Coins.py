# cook your dish here
for i in range(int(input())):
    x,y=map(int,input().split())
    ans=x+(y*2)
    
    if (x!=0 and ans%2==0) or (x==0 and y%2==0):
        print('YES')
    else:
        print('NO')