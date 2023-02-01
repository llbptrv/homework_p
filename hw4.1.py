N = int(input('Количество чисел:'))
a=[0]*N

from random import randint
for i in range(N):
    a[i]=randint(0,10)
print(a)    

unique_a = list(set(a))
unique_a.sort()
print(unique_a)

M = int(input('Количество чисел:'))
b=[0]*M

from random import randint
for i in range(M):
    b[i]=randint(0,10)
print(b)  

unique_b = list(set(b))
unique_b.sort()
print(unique_b)