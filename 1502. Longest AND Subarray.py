# cook your dish here
# cook your dish here
T = int(input())

for tc in range (T):
    N = int(input())
    ans = 0
    temp = 1
    for i in range (31,-1,-1):
        if (N>>i & 1 == 1):
            ans = 1<<i
            if (i != 0):
                temp = 1<<(i-1)
            break
    print(max(N-ans+1,temp))