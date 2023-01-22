print("введите сумму:")
s=int(input())
print("введите произведение:")
p=int(input())

x = (s-int((s**2-4*p)**0.5))//2
y = (s+int((s**2-4*p)**0.5))//2
print(x, y)