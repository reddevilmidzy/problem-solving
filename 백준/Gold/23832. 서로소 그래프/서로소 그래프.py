import sys
input = sys.stdin.readline

def euler_phi(n):
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

ans = 0

n = int(input())
for i in range(2, n+1):
    ans += euler_phi(i)
print(ans)