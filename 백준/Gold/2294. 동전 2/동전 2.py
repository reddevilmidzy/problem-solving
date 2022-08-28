import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coin = []
INF = int(1e7)
dp = [INF]*(k+1)
for _ in range(n):
    c = int(input())
    if c <= k and c not in coin:
        coin.append(c)
        dp[c] = 1
coin.sort()
for i in range(1, k+1):
    ans = 0
    for j in coin:
        if i<j:
            break
        dp[i] = min(dp[i], dp[i-j]+1)
print(dp[k] if dp[k] != INF else -1)