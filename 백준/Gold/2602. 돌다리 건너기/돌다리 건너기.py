s = input().rstrip()
angel = input().rstrip()
devil = input().rstrip()
m = len(s)
n = len(angel)

dp = [[[0]*m for _ in range(n)] for _ in range(2)]

for i in range(n):
    if angel[i] == s[0]:
        dp[0][i][0] = 1
    if devil[i] == s[0]:
        dp[1][i][0] = 1

ans = 0

for i in range(n):
    for j in range(m):
        if dp[0][i][j]:
            if j == m-1:
                ans += dp[0][i][j]
            else:
                for k in range(i+1, n):
                    if devil[k] == s[j+1]:
                        dp[1][k][j+1] += dp[0][i][j]
        if dp[1][i][j]:
            if j == m-1:
                ans += dp[1][i][j]
            else:
                for k in range(i+1, n):
                    if angel[k] == s[j+1]:
                        dp[0][k][j+1] += dp[1][i][j]

print(ans)