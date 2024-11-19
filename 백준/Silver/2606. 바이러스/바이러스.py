import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
com = int(input().rstrip())
visited = [False] * (com+1) # 컴퓨터갯수와 곱함
connect = []
lan = int(input().rstrip())
graph = [[] for i in range(com+1)]

for i in range(lan):
    connect.append(list(map(int, input().rstrip().split())))

for j in connect:
    for k in range(1, com+1):
        if k in j:
            graph[k].append(*set(j)-{k})

dfs(graph, 1, visited)
print(visited.count(True)-1)