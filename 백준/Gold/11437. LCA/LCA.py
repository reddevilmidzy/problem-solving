import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
parent = [0] * (n+1)
d = [0] * (n+1)
c = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 부모 저장
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]:
            continue
        parent[y] = x
        dfs(y, depth+1)


def lca(a, b):
    # 깊이 같게 설정
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    
    # 같이 올라감
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0)


m = int(input())    
for _ in range(m):
    a,b = map(int,input().split())
    print(lca(a, b))