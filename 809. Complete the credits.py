# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    if x==65:
        print("normal")
    elif(x>65):
        print("overload")
    elif(x<35):
        print("underload")
    else:
        print("normal")