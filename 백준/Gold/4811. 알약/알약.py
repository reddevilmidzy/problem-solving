import sys
input = sys.stdin.readline
# 카탈란수 그게뭔데씹덕아..

m = 31
dp = [0]*(m+1)
dp[0] = 1
dp[1] = 1

for i in range(1, m+1):
    tmp = 0
    for j in range(i):
        tmp += dp[j]*dp[i-j]
    dp[i] = tmp

while True:
    n = int(input())
    if not n:break
    print(dp[n+1])