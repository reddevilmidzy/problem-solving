# dfs 로 해결

import sys
input = sys.stdin.readline

def find(parent:list[int], x:int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent:list[int], u:int, v:int) -> None:
    u = find(parent, u)
    v = find(parent, v)

    if u < v:
        parent[v] = u
    else:
        parent[u] = v

def union_find(edges:list[int,int]):
    parent = [i for i in range(n+1)]
    cnt = n-1
    blue = 0
    for c,u,v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            cnt -= 1
            blue += c
            if not cnt:
                break
    
    return blue

def dfs(u:int, v:int) -> bool:
    global graph
    stk = [(u, 0, 0)]
    visited = [False]*(n+1)
    visited[u] = True
    while stk:
        cur,x,y = stk.pop()
        if cur == v:
            # u,v 연결할 수 있음
            # 왜냐? 사이에 R 간선이 있기 때문
            if x and y:
                # 여기 시복 에반ㄷ
                graph[x].remove((0,y))
                graph[y].remove((0,x))

                graph[u].append((1,v))
                graph[v].append((1,u))

                if (x,y) in use:
                    use.remove((x,y))
                else:
                    use.remove((y,x))

                use.add((u,v))

                return True
            return False
        
        for is_blue, nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                if not is_blue:
                    stk.append((nxt, cur, nxt))
                else:
                    stk.append((nxt, x, y))


    return

n,m,k = map(int,input().split())
edges = []

for _ in range(m):
    c,u,v = input().rstrip().split()
    u = int(u)
    v = int(v)
    edges.append((+(c=="B"), u, v))

edges.sort()

min_mst = union_find(edges)
max_mst = union_find(edges[::-1])
# print(min_mst, max_mst)
# print("k", k)

if min_mst > k or max_mst < k:
    print(0)
    exit()

parent = [i for i in range(n+1)]
cnt = n-1
use = set()

graph = [[] for _ in range(n+1)]
cur_blue = 0

for c,u,v in edges:
    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        cnt -= 1
        if c: cur_blue += 1

        graph[u].append((c, v))
        graph[v].append((c, u))
        use.add((u,v))

        if not cnt: break

mst = max_mst
need = k - cur_blue


# print(graph)
# print("need",need, "cur_blue", cur_blue)
for c,u,v in edges[::-1]:
    if not c: break
    if not need: break
    
    if dfs(u,v):
        need -= 1

for u,v in sorted(use):
    print(u,v)