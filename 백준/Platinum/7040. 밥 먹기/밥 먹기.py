import sys
input = sys.stdin.readline
INF = float('inf')

def bellman_ford(st: int, ed: int):
    distance = [INF] * (n + 1)
    distance[st] = 0

    for _ in range(n - 1):
        for cur in range(1, n + 1):
            for nxt, val in graph[cur]:

                if distance[nxt] > distance[cur] + val:
                    distance[nxt] = distance[cur] + val
    
    flag = True
    for cur in range(1, n + 1):
        for nxt,val in graph[cur]:
            if distance[nxt] > distance[cur] + val:
                # 무한 사이클
                flag = False

    if flag:
        return distance[ed] if distance[ed] != INF else -2
    return -1

n,m,k = map(int,input().split())
# 소수, 좋아하는지, 싫어하는지
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

for _ in range(k):
    u,v,w = map(int,input().split())
    graph[v].append((u,-w))

for i in range(1, n):
    graph[i+1].append((i, 0))

print(bellman_ford(1, n))