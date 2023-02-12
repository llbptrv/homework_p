n = int(input('Количество элементов массива: '))
a = [0]*n
a[0] = int(input('Первый элемент: '))
d = int(input('Разность: '))
print(a[0],end=' ')
for i in range(1,n):
    a[i]= a[i-1]+d
    print(a[i],end=' ')