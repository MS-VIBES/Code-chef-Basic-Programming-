# cook your dish here
choose=int(input())
for c in range(choose):
  a,b=map(int,input().split())
  if (a+b)%2==0: print("Bob")
  else: print("Alice")