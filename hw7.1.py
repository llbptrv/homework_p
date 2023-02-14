def f(words):
    return sum(1 for i in words if i in 'аеёиоуыэюя')
    
    
c = "пара-ра-рам рам-пам-папам па-ра-па-да"
st = c.lower().split()
t = f(st[0])
if all([f(i) == t for i in st]):
    print('Парам пам-пам')
else:
    print('Пам парам')