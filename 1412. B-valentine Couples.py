# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a_height=list(map(int,input().split()))
    b_height=list(map(int,input().split()))
    boys=sorted(b_height)
    girls=sorted(a_height,reverse=True)
    max_value=0
    for i in range(n):
        if boys[i] + girls[i] > max_value:
            max_value=boys[i]+girls[i]
    print(max_value)