# cook your dish here
medal=int(input())
for m in range(medal):
  a,b,c,d,e,f=map(int,input().split())
  if (a+b+c)>(d+e+f): print(1)
  else: print(2)