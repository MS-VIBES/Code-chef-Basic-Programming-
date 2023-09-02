# cook your dish here
T = int(input())

for _ in range(T):
    n = int(input())
    
    m = n // 2
    
    if n % 4 == 2 or n == 2:
        print('NO')
    else:
        print('YES')
        for i in range(1, m, 2):
            print(i, end = ' ')
        for i in range(m + 2, n + 1, 2):
            print(i, end = ' ')
        
        print()
        
        for i in range(2, m + 1, 2):
            print(i, end = ' ')
        for i in range(m + 1, n, 2):
            print(i, end = ' ')
        
        print()
        