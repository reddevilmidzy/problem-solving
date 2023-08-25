primes = [False, False] + [True]*999999

for i in range(2,int(1000000**0.5)+1):
    if primes[i] == True:
        for j in range(i*2, 1000001, i):
            primes[j] = False

for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(2, n//2+1):
        if primes[i] and primes[n-i]:
            ans += 1
    print(ans)