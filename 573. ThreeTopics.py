# cook your dish here

a,b,c,x=map(int,input().split())
abc=list((a,b,c))
if x in abc:
    print("YES")
else:
    print("NO")