# cook your dish here
testcase=int(input())
for _ in range(testcase):
    a=int(input())
    if a%2==0 and a%7==0:
        print("Alice")
    elif a%2==1 and a%9==0:
        print("Bob")
    else:
        print("Charlie")