a,b,c,k = map(int,input().split())
turn = [a,b,c]
INF = int(1e9)
dp = [[INF]*4 for _ in range(k+1)]
dp[0][0] = 0
move = [3,1,2]
for i in range(k+1):
    for j in range(4):
        if dp[i][j] == INF:
            continue
        for w in range(3):
            if i + turn[w] > k:
                continue
            dp[i + turn[w]][(j + move[w]) % 4] = min(dp[i + turn[w]][(j+move[w])%4], dp[i][j] + 1)
print(dp[k][0] if dp[k][0] != INF else -1)