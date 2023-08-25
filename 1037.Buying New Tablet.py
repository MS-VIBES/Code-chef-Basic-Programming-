# cook your dish here
T = int(input())
for tc in range(T):
    # n=number of tablets, b=budget
    (n, b) = map(int, input().split(' '))
    
    sel = []   # selection
    for i in range(n):
        # width, height, price
        (w, h, p) = map(int, input().split(' '))
        
        if p <= b: # within budget
            sel.append(w*h)
    
    if len(sel) == 0:
        print("no tablet")
    else:
        print(max(sel))
            