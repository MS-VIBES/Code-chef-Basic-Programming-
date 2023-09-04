# cook your dish here
T = int(input())

for tc in range (T):
    N = int(input())
    A = list(map(int, input().split()))
    i = 0
    j = N - 1
    f = 0
    c = 1
    while (i<=j):
        if ((A[i] == A[j]) and (A[i] == c)):
            i += 1
            j -= 1
        else:
            c += 1
            if ((A[i] == A[j]) and (A[i] == c)):
                i += 1
                j -= 1
            else:
                f = 1
                break
        if (c > 7):
            f = 1
            break
    if (f == 0 and c == 7):
        print('yes')
    else:
        print('no')