# cook your dish here
T = int(input())

for tc in range (T):
    N,K,L = map(int, input().split())
    c = 0
    if (N > K*L or (K == 1 and N > 1)):
        print(-1)
    else:
        for i in range (L):
            for j in range (K):
                if (c < N):
                    print(j+1,end = ' ')
                    c += 1
                else:
                    break
            if (c < N):
                continue
            else:
                break
    print()