mod = int(1e9)+7
def factorial(n:int) -> int:
    res = 1
    for i in range(1, n+1):
        res = (res*i)%mod
    return res

def multi(num: int, n:int) -> int:
    if n == 0:
        return 1
    elif n%2 == 0:
        val = multi(num, n//2) % mod
        return (val**2)%mod
    else:
        return (multi(num, n-1) * num) % mod
n,k = map(int,input().split())

a = factorial(n)
b = (factorial(k) * factorial(n-k))%mod
b = multi(b, mod-2)

print(((a%mod)*(b%mod))%mod)