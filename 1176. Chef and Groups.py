# cook your dish here
for _ in range(int(input())):
    s=input().split("0")
    count=0
    for i in s:
        if (i!=""):
            count+=1 
    print(count)