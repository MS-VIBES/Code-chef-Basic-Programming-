for _testcase in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = input()
    x = []
    for i in range(n):
        if (b[i]) == '0':
            x.append(a[i])
            
    print(min(x))