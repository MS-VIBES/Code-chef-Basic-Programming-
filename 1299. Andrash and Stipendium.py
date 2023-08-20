# cook your dish here
for _ in range(int(input())):
    n=int(input())
    scores=list(map(int,input().split()))
    if 2 in scores:
        print("No")
        continue
    elif (5 not in scores):
        print("No")
        continue
    else:
        total=sum(scores)/n
        if total >= 4:
            print("Yes")
        else:
            print("No")