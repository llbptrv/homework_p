
N = int(input('Количество чисел:'))
a=[0]*N

from random import randint
for i in range(N):
    a[i]=randint(0,10)
print(a)    


x=int(input('Заданное число:'))
b=[abs(a[i]-x) for i in range(len(a))]
print(a[b.index(min(b))])