from collections import defaultdict

mod = int(1e9)+7
n = int(input())
d = defaultdict(int)

def fibo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if d[n] > 0:
        return d[n]
    if n % 2 == 1:
        m = (n+1)//2
        t1 = fibo(m)
        t2 = fibo(m-1)
        d[n] = t1*t1 + t2*t2
        d[n] %= mod
        return d[n]
    m = n//2
    t1 = fibo(m-1)
    t2 = fibo(m)
    d[n] = (2*t1 + t2) * t2
    d[n] %= mod
    return d[n]

print(fibo(n))