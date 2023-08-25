# cook your dish here
for i in range(int(input())):
    n,m=input().split()
    n=int(n)
    lad=0
    for i in range(n):
        li=list(input().split())
        if 'WON' in li[0]:
            if int(li[1])<=20:
                lad+=(300+(20-int(li[1])))
            else:
                lad+=300
        if 'TOP' in li[0]:
            lad+=300
        if 'BUG' in li[0]:
            if int(li[1])>=50 and int(li[1])<=1000:
                lad+=int(li[1])
        if 'HOSTED' in li[0]:
            lad+=50
            
    if m=='INDIAN':
        print(lad//200)
    else:
        print(lad//400)