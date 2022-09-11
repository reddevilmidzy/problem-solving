import sys
input = sys.stdin.readline

INF = int(1e9)
n,m,r = map(int,input().split())
items = [0]
items.extend(list(map(int,input().split())))
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(r):
    a,b,l = map(int,input().split())
    graph[a][b] = min(l, graph[a][b])
    graph[b][a] = min(l, graph[b][a])


for x in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j:
                continue
            graph[i][j] = min(graph[i][x]+graph[x][j], graph[i][j])

res = []
for i in range(1,n+1):
    ans = items[i]
    for j in range(1,n+1):
        if graph[i][j] != int(1e9) and graph[i][j] <= m:
            # print('i',i,'j',j,graph[i][j],items[j])
            ans += items[j]
    # print(ans)
    res.append(ans)

    # res = max(res, ans)
print(max(res))