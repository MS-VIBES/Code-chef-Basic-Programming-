# cook your dish here
cont=int(input())
for c in range(cont):
  a,b,c,d=map(int,input().split())
  chef=a+(10*c)
  chefina=b+(10*d)
  if chef<chefina: print("chef")
  elif chef>chefina: print("chefina")
  else: print("draw")