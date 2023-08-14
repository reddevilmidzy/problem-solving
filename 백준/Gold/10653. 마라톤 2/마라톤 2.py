import sys
input = sys.stdin.readline
INF = int(1e9)

def dist(a:list[int], b:list[int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

n,k = map(int,input().split())
pos = [list(map(int,input().split())) for _ in range(n)]
distance = [[dist(pos[i], pos[j]) for j in range(n)] for i in range(n)]
dp = [[INF]*n for _ in range(k+1)]
dp[0][0] = 0

for i in range(1, n):
    dp[0][i] = dp[0][i-1] + distance[i-1][i]

for i in range(1, k+1):
    for j in range(1, n):
        for o in range(i, 0, -1):
            if j-o >= 0:
                dp[i][j] = min(dp[i][j], dp[i-o][j-o-1]+distance[j][j-o-1], dp[i][j-1]+distance[j-1][j])

print(dp[-1][-1])