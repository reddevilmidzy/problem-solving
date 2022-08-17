import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

def dfs(tree, v, visited):
    global node,dis
    for i in tree[v]:
        if visited[i[0]] == -1:
            visited[i[0]] = i[1] + visited[v]
            if visited[i[0]] > node:
                node = visited[i[0]]
                dis = i[0]
            dfs(tree, i[0], visited)
            
if n == 1:
    print(0)
else:
    tree = {}
    for i in range(1, n+1):
        tree[i] = []

    for _ in range(n-1):
        a,b,c = map(int,input().split())
        tree[a].append([b,c])
        tree[b].append([a,c])

    for i in range(1,n+1):
        if len(tree[i]) == 1:
            x = tree[i][0][0]
            visited = [-1]*(n+1)
            visited[x] = 0
            node,dis = 0,0
            dfs(tree, x, visited)
            break
    visited = [-1]*(n+1)
    visited[dis] = 0
    dfs(tree, dis, visited)
    print(node)