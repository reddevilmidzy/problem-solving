import sys
input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return 0
    return 1

while True:
    n = int(input().rstrip())
    if n == 0:
        break
    arr = [i for i in range(n+1, 2*n+1) if i%2 != 0 or i==2]
    ans = 0
    for k in arr:
        ans += is_prime(k)
    print(ans)