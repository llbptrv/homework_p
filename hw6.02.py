print("введите число элементов:")
n=int(input())
list1=[0]*n
from random import randint
for i in range(n):
    list1[i]=randint(0,10)
print(list1)

maxi=int(input("MAX= "))
mini=int(input("MIN= "))
list2=[]
if maxi>=mini:
  for i in range(len(list1)):
    if maxi>=list1[i] and mini<=list1[i]:
      list2.append(list1[i])
  print(list2)