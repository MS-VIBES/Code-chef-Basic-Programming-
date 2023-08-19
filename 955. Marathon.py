# cook your dish here
for _ in range(int(input())):
    D,d,A,B,C=map(int,input().split())
    res=d*D 
    prize=0 if res<10 else(C if res>=42 else (B if res>=21 else A))
    print(prize)