goals = int(input())
for i in range(goals):
    aim = int(input())
    life = list(map(int, input().split()))
    wife = {}
    for death in life:
        if death not in wife:
            wife[death] = 1
        else:
            wife[death] += 1
    for j in wife:
        if wife[j] <= 2:
            continue
        else:
            print('No')
            break
    else:
        print('Yes')