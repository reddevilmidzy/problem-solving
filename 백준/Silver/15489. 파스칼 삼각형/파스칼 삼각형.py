import sys
input= sys.stdin.readline
r,c,w = map(int,input().split())

dp = [[1] for _ in range(r+w+2)]
for i in range(1,r+w+2):
    for j in range(1,len(dp[i-1])):
        dp[i].append(dp[i-1][j-1]+dp[i-1][j])
    dp[i].append(1)

ans = 0
tmp = 0
for i in range(r-1, r+w-1):
    ans += sum(dp[i][c-1:c+tmp])
    tmp += 1
print(ans)