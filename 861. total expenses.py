for _ in range(int(input())):
    a,b=map(int,input().split())
    if a>1000:
        x=a-(a*0.10)
        print(x*b)
    else:
        print(a*b)
    