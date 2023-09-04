import sys
input = sys.stdin.readline

def z_fun(s:str):
    n = len(s)
    z = [0]*n
    z[0] = n
    r = 0
    l = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r-i+1, z[i-l])
        while i+z[i] < n and s[i+z[i]] == s[z[i]]:
            z[i] += 1
        if r < i+z[i]-1:
            r = i+z[i]-1
            l = i
    return z

z = z_fun(input().rstrip()[::-1])
n = len(z)
m = int(input())
for _ in range(m):
    print(z[n-int(input())])