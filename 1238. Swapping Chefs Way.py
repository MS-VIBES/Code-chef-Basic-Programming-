# cook your dish here
# cook your dish here
T = int(input())

for tc in range (T):
    N = int(input())
    S = list(input())
    P = sorted(S) 
    if (P != S):
        for i in range(N // 2): 
            if S[i] > S[N - 1 - i]:
                S[i], S[N - i - 1] = S[N - 1 - i], S[i]
    if (P == S):
        print('YES')
    else:
        print('NO')