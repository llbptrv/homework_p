#колчество кустов на грядке
from random import randint
a=randint(3,10)
print(a)
#количество ягод на каждом кусту
kyst=[0]*a
for i in range(a):
    kyst[i]=randint(0,10)
print(kyst)  
#считаем ягоды
max=0
for i in range(len(kyst)-1):
   n=kyst[i-1]+kyst[i]+kyst[i+1]

   if n>max:
    max=n
    n+=1
print(max)
