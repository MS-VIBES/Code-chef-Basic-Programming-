t=int(input())
for i in range(t):
    n=int(input())
    s=str(input())# cook your dish here
    l=list(s)
    alice=0
    bob=0
    server = 'ALICE'
    for i in range(n):
        if s[i] == server[0]:
            # Server wins the point
            if server == 'ALICE':
                alice+= 1
            else:
                bob += 1
        else:
            if server == 'ALICE':
                server = 'BOB'
            else:
                server = 'ALICE'
    print(alice,bob)