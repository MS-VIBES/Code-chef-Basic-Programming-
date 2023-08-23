# cook your dish here
for _ in range(int(input())):
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    score_A=0
    for i in range(3):
        if A[i]>B[i]:
            score_A+=1
    if score_A>=2:
        print('A')
    else:
        print('B')