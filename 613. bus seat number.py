# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    if n>=1 and n<=10:
        print("Lower Double")
    elif n>=16 and n<=25:
        print("Upper Double")
    elif n>=11 and n<=15:
        print("Lower Single")
    else:
        print("Upper Single")