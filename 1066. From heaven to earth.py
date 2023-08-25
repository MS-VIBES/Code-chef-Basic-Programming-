t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    s=b*2**0.5/(a)
    e=c/a
    print("Stairs" if e<s else "Elevator")