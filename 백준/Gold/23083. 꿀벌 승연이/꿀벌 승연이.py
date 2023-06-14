import sys
input = sys.stdin.readline

mod = int(1e9)+7
d = [((0,1), (1,1), (1,0)), ((1,0), (0,1), (-1,1))]

n,m = map(int,input().split())
k = int(input())
visited = [[0]*(m+1) for _ in range(n+1)]

for _ in range(k):
    r,c = map(int,input().split())
    visited[r][c] = -1

visited[1][1] = 1

for c in range(1, m+1):
    for r in range(1, n+1):
        if visited[r][c] == -1: continue
        for dy,dx in d[c%2]:
            ny,nx = dy+r,dx+c
            if ny < 1 or nx < 1 or ny > n or nx > m: continue
            if visited[ny][nx] == -1: continue # 구멍
            visited[ny][nx] += visited[r][c]
            visited[ny][nx] %= mod
print(visited[n][m])