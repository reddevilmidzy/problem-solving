import sys
input = sys.stdin.readline

INF = int(1e9)
n= int(input())
graph = [[] for _ in range(n)]
dist = [[INF]*(n) for _ in range(n)]
while True:
    a,b = map(int,input().split())
    if a==-1 and b==-1:
        break
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(n):
    for j in range(len(graph[i])):
        dist[i][graph[i][j]] = 1

for x in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                dist[i][j] = 0
            else:
                # graph[i]
                dist[i][j] = min(dist[i][x]+dist[x][j], dist[i][j])
ans = [0]*(n)
for i in range(n):
    ans[i] = max(dist[i])

min_ans = min(ans)
print(min_ans, ans.count(min_ans))
for i in range(n):
    if ans[i] == min_ans:
        print(i+1,end=' ')