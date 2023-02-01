print("введите число элементов:")
n=int(input())
print("введите число:")
k=int(input())
count=0
list1=[0]*n
from random import randint
for i in range(n):
    list1[i]=randint(0,5)
print(list1)

for i in range(len(list1)):
    if list1[i]==k:
        count+=1
        

print(count)

if count==0:
    print("нет такого значения")


