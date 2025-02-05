import sys
input = sys.stdin.readline

n,k = map(int,input().split())
back =[[0,0]]+ [list(map(int,input().split())) for _ in range(n)]
dp = [0]*(k+1)

for i in range(1, n+1):
    for j in range(k, 0, -1):
        if back[i][0] <= j:
            dp[j] = max(dp[j], dp[j-back[i][0]]+back[i][1])

print(dp[k])