import sys
input = sys.stdin.readline
prime = []
def prime_list(n):
    sieve = [True]*n
    global prime
    m = int(n**0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    prime = [i for i in range(2, n) if sieve[i] == True]
    return prime

prime_list(10000)

for t in range(int(input())):
    N = int(input())
    abss = 10000
    a, b = 0,0
    for p in prime:
        if N-p in prime:
            if abss > abs(p-(N-p)):
                abss = abs(p-(N-p))
                a = min(p, N-p)
                b = max(p, N-p)
        if N < p:
            break
    print(a,b)