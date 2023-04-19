def solve():
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                dp[i][j] += dp[i][j-1]
            elif j == 0:
                dp[i][j] += dp[i-1][j]
            else:
                dp[i][j] += dp[i-1][j] + dp[i][j-1]

            if (i,j) in construc:
                for py, px in set(construc[(i,j)]):
                    dp[i][j] -= dp[py][px]

    return dp[n][m]

m,n = map(int,input().split())
k = int(input())

construc = dict()
for _ in range(k):
    a,b,c,d = map(int,input().split()) # 가로 세로
    a,c = min(a,c), max(a,c)
    b,d = min(b,d), max(b,d)
    if (d,c) in construc:
        construc[(d,c)].append((b,a))
    else:
        construc[(d,c)] = [(b,a)]

print(solve())