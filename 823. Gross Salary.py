# cook your dish here
salary=int(input())
for s in range(salary):
  basic=int(input())
  if basic>=1500:
    print(basic+500+0.98*basic)
  else:
    print(basic+0.1*basic+0.9*basic)