"""
Pattern is
1
22
333
4444
55555"""

n=int(input("enter number of rows :"))
for i in range(1,n+1):
  for i in range(1,i+1):
    print(i,end="")
  print()
