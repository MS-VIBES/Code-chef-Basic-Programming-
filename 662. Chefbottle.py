# cook your dish here
T = int(input())
for i in range(T):
    N, X, K = map(int, input().split())
    A = K // X
    print(min(N, A))