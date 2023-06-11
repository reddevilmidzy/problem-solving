from math import log2, ceil
n = int(input())
tot = ceil(log2(n))
ans = 0

if 2**tot == n: # 안자름
    pass
else:
    for i in range(tot, -1, -1):
        if n >= 2**i:
            n -= 2**i
            ans = i
    ans = tot-ans

print(2**tot, ans)