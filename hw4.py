print("введите m")
m=int(input())
print("введите n")
n=int(input())
print("введите k")
k=int(input())

if (k<=n*(m-1) or k<=m*(n-1)) and (k>=n or k>=m):
    print("yes")
else:
    print("no")
