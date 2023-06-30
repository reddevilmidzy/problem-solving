from math import gcd

a,b = map(int,input().split())
c,d = map(int,input().split())

x = a*d + c*b
y = b*d

while gcd(x,y) != 1:
    x,y = x//gcd(x,y), y//gcd(x,y)
print(x,y)