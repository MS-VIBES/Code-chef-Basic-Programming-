t=int(input())
for _ in range(t):
    n=int(input())
    a=[]
    for j in range(n):
        a.append(input())
    if "cakewalk" in a:
        if "simple" in a:
            if "easy" in a:
                if "easy-medium" in a or "medium" in a:
                    if "medium-hard" in a or "hard" in a:
                        print("Yes")
                    else:
                        print("No")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
        
        
        
        
        