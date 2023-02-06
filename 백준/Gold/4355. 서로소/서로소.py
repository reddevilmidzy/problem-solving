import sys
input = sys.stdin.readline

def euler_phi(n):
    if n == 1:
        return 0
    i = 2
    ret = n
    while i*i <= n:
        if n%i==0:
            while n%i==0:
                n //= i
            ret -= ret//i
        i += 1
    if n > 1:
        ret -= ret//n
    
    return ret

while True:
    n = int(input())
    if n == 0:
        break
    print(euler_phi(n))