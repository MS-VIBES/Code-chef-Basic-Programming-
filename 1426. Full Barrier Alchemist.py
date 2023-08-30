# cook your dish here
for _ in range(int(input())):
    n,h,y1,y2,l=map(int,input().split())
    count=0
    for j in range(n):
        t,x=map(int,input().split())
        if (t==1 and x>=h-y1)or(t==2 and x<=y2):
            count+=1
        else:
            count+=1
            l-= 1 
        if l<=0:
            count-=1 
    print(count)
            