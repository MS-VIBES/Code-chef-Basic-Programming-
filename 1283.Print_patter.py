
for _ in range(int(input())):

    N = int(input())
    
    m = []
    for i in range(N):
        m.append([0] * N)
        
    cnt = 1
    
    for i in range(N):
        
        x = 0
        y = i
        
        while True:
            m[x][y] = cnt
            cnt += 1
            
            if y == 0:
                break
            x += 1
            y -= 1
            
    for i in range(N - 1):
        x = i + 1
        y = N - 1
        
        while True:
            m[x][y] = cnt
            cnt += 1
            
            if x == N - 1:
                break
            x += 1
            y -= 1
            
        
    for i in range(N):
        for j in range(N):
            print(m[i][j], ' ', end="")
        print()