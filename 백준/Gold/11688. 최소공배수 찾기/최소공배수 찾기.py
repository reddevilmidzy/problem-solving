import math

a,b,L = map(int,input().split())

def divisor(n):
    can = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i==0:
            can.append(i)
            can.append(n//i)
    return sorted(can)


if math.lcm(a,b) == L:
    print(1)
elif L%math.lcm(a,b)!=0:
    print(-1)
else:
    ab = math.lcm(a,b)
    for c in divisor(L):
        if math.lcm(ab, c)==L:
            print(c)
            break