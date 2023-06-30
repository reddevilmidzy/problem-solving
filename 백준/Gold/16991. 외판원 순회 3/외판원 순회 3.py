from sys import stdin
input = stdin.readline
INF = 1e9

def find_path(current_city, visited):
    if visited == (1 << n) - 1:
        return graph[current_city][0] or INF
    if dp[current_city][visited]:
        return dp[current_city][visited]
    tmp = INF
    for next_city in range(n):
        if not visited & (1 << next_city) and graph[current_city][next_city]:
            tmp = min(tmp, find_path(next_city, visited | (1 << next_city)) + graph[current_city][next_city])
    dp[current_city][visited] = tmp
    return tmp

n = int(input())
pos = [list(map(int,input().split())) for _ in range(n)]

graph = [[0]*n for _ in range(n)]
dp = [[None] * (1 << n) for _ in range(n)]

for i in range(n):
    x,y = pos[i]
    for j in range(i+1, n):
        r,c = pos[j]
        graph[i][j] = graph[j][i] = ((x-r)**2 + (y-c)**2)**0.5

print(find_path(0, 1<<0))