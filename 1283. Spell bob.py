# cook your dish here
for _ in range(int(input())):
    tf, bf = input(), input()
    lb, lo, ot = 0, 0, 0
    for a,b in zip(tf, bf):
        if a == 'b' or b == 'b': lb += 1
        if a == 'o' or b == 'o': lo += 1
        if a != 'b' and a != 'o' and b != 'b' and b != 'o': ot += 1
    #print( lb, lo, ot)
    print('yes' if ot == 0 and lo >= 1 and lb >= 2 else 'no')