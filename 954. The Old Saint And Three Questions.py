for _testcase in range(int(input())):
    a,b,c = map(int, input().split())
    d,e,f, = map(int, input().split())
    if (a + b + c) == (d + e + f): print('Pass')
    else: print('Fail')