# cook your dish here
mix=int(input())
for m in range(mix):
  a,b=map(int,input().split())
  if a>0 and b>0: print("Solution")
  else: print("Liquid") if a==0 else print("Solid")