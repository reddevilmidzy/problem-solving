import sys
input = sys.stdin.readline

n = int(input())
graph = []
dp = [[0 for i in range(n)] for j in range(n)]
dp[0][0] = 1
for i in range(n):
    graph.append(list(map(int,input().rstrip().split())))

for i in range(n):
    for j in range(n):
        if dp[i][j] != 0 and graph[i][j] != 0:
            move = graph[i][j]
            if -1 < i + move < n:
                dp[i+move][j] += dp[i][j] 
            if -1 < j+ move < n:
                dp[i][j+move] += dp[i][j]
        
print(dp[n-1][n-1])