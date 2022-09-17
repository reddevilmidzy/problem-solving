import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

# [가로,세로,대각선] 의 방문 개수
dp = [[[0,0,0] for _ in range(n)] for _ in range(n)]
# 시작은 가로(끝점에만 기록)
dp[0][1][0] = 1

for i in range(n):
    for j in range(1,n):
		# 이전에 방문한 곳만 방문 가능
        if sum(dp[i][j]) != 0:
            row = False
            col = False
            if j+1 < n and graph[i][j+1]!=1:
                col = True
                dp[i][j+1][0] = dp[i][j][0]+dp[i][j][2]
            if i+1 < n and graph[i+1][j]!=1:
                row = True
                dp[i+1][j][1] = dp[i][j][1]+dp[i][j][2]
            if row and col and graph[i+1][j+1]!=1:
                dp[i+1][j+1][2] = dp[i][j][0]+dp[i][j][1]+dp[i][j][2]
                
print(sum(dp[n-1][n-1]))