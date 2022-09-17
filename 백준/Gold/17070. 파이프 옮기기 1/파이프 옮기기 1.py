import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

dp = [[[0,0,0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
#print(dp)

for i in range(n):
    for j in range(n):
        if sum(dp[i][j]) != 0:
            first = False
            second = False
            three = False
            if j+1 < n and graph[i][j+1]!=1:
                first = True
                dp[i][j+1][0] = dp[i][j][0]+dp[i][j][2]
                #print('chekc')
            if i+1 < n and graph[i+1][j]!=1:
                second = True
                dp[i+1][j][1] = dp[i][j][1]+dp[i][j][2]
                #print('chekc2')
            if i+1<n and j+1<n and graph[i+1][j+1]!=1 and first and second:
                dp[i+1][j+1][2] = dp[i][j][2]
                three = True
                #print('chekc3')
            
            if three:
                #print('chekaaaaa')
                dp[i+1][j+1][2] = dp[i][j][0]+dp[i][j][1]+dp[i][j][2]
# print(dp)    
print(sum(dp[n-1][n-1]))