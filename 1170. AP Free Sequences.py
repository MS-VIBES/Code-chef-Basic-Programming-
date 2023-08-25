T = int(input())

for _ in range(T):
    N = int(input())
    sequence = list(map(int, input().split()))

    isAPFree = True

    for i in range(N):
        for j in range(i + 1, N):
            diff = sequence[j] - sequence[i]
            next_term = sequence[j] + diff
            if next_term in sequence:
                isAPFree = False
                break
        if not isAPFree:
            break

    if isAPFree:
        print("YES")
    else:
        print("NO")