goals = int(input())
for distractions in range(goals):
    wife, life, aim = map(int, input().split())
    List = list(map(int, input().split()))
    knife = List.count(life) / wife
    death = List.count(aim) / wife
    print(knife * death)