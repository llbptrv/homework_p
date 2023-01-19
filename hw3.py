a=int(input())
b=a%1000
c=a//1000

n=b%10
m=b//100
k=(b//10)%10
s1=n+m+k

n1=c%10
m1=c//100
k1=(c//10)%10
s2=n1+m1+k1

if s1==s2:
    print("yes")
else:
    print("no")