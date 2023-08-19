for i in range(int(input())):
    lst=list(map(int,input().split()))
    if lst[0] is min(lst):
        print("Draw")
    elif(lst[1] is min(lst)):
        print("Bob")
    else:
        print("Alice")