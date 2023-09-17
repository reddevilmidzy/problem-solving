import sys
input = sys.stdin.readline

n,k = map(int,input().split())
m = 100
s = list(map(int,input().split()))
h = list(map(int,input().split()))

dp = [[0]*(m+1) for _ in range(n)]

for i in range(n):
    for j in range(m+1):
        cur = min(100, j+k)
        if cur >= h[i]:
            dp[i][cur-h[i]] = max(dp[i][cur-h[i]], dp[i-1][j]+s[i])        
        dp[i][cur] = max(dp[i][cur], dp[i-1][j])

print(max(dp[n-1]))