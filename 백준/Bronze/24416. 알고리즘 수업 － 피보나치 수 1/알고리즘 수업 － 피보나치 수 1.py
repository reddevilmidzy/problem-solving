def fibo2(n):
    ans = -1
    for i in range(2, n+1):
        ans += 1
    return ans

def fibo1(n):
    f=[0 for i in range(n)]
    f[0], f[1] = 1,1
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]

    return f[-1]
n = int(input())
print(fibo1(n), fibo2(n))