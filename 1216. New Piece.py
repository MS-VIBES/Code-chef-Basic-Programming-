# cook your dish here
t=int(input())
for _ in range(t):
    a,b,p,q=map(int,input().split())
    sum_a=a+b 
    sum_b=p+q
    div_a=sum_a%2
    div_b=sum_b%2
    if a==p and b==q:
        print(0)
    elif div_a == div_b:
        print("2")
    else:
        print("1")
        


    