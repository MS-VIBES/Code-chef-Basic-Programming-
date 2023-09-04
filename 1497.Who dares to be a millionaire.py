# cook your dish here
for _ in range(int(input())):
    n=int(input())
    correct_ans=input()
    chef_ans=input()
    w=list(map(int,input().split()))
    c=0
    m=w[0]
    for i in range(n):
        if (correct_ans[i] == chef_ans[i]):
            c+= 1 
        if (w[c]>m):
            m=w[c]
    if (n==c):
        print(w[n])
    else:
        print(m)
    

  