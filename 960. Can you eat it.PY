# cook your dish here
bite=int(input())
for b in range(bite):
  n,k=map(int,input().split())
  if n%k==0: print(n//k)
  else: print(-1)