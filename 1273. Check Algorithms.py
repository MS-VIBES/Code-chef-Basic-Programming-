# cook your dish here
T = int(input())

for tc in range (T):
    S = input()
    compressed = ""
    count = 1
    for i in range(1, len(S)):
        if (S[i] == S[i - 1]):
            count += 1
        else:
            compressed += S[i - 1] + str(count)
            count = 1
    compressed += S[-1] + str(count)
    if (len(compressed) < len(S)):
        print("YES")
    else:
        print("NO")