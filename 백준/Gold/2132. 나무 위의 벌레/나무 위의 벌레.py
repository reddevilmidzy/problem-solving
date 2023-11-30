import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

res = -1
node = 0

def dfs(cur, cnt):
    global tmp, node
    if tmp < cnt:
        tmp = cnt
        node = cur
    elif tmp == cnt:
        node = min(node, cur)
    
    for nxt in graph[cur]:

        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, cnt + arr[nxt])
            visited[nxt] = False

tmp = -1
node = 0

visited[n] = True
dfs(n, arr[n])
visited[n] = False

tmp = -1
pre_node = node
visited[pre_node] = True
node = 0
dfs(pre_node, arr[pre_node])

print(tmp, min(pre_node, node))