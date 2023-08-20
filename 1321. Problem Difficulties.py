# cook your dish here
T = int(input())

for tc in range (T):
    A = list(map(int, input().split()))
    A.sort()
    if (A[1] != A[2] or (A[1] == A[2]and A[0] != A[1]and A[2] != A[3])):
        print('2')
    elif (A[0] == A[3]):
        print('0')
    else:
        print('1')
        