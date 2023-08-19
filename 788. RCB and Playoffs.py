# cook your dish here
play=int(input())
for p in range(play):
  x,y,z=map(int,input().split())
  print("yes") if x+2*z>=y else print("no")