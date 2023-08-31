from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur:int):
    global idx, num

    idx += 1
    d[cur] = idx
    visited[cur] = True
    stk.append(cur)

    parent = d[cur]

    for nxt in graph[cur]:
        if d[nxt] == -1:
            parent = min(parent, dfs(nxt))
        elif visited[nxt]:
            parent = min(parent, d[nxt])
    
    if d[cur] == parent:
        cnt = 0
        while True:
            node = stk.pop()
            visited[node] = False
            scc_idx[node] = num
            cnt += edges_cnt[node]
            if cur == node: break

        scc_node[num] = cnt
        num += 1

    return parent

def topology(dag:list[list[int]], edges:list[int]) -> list[int]:
    global first, second
    queue = deque()
    level = [0]*num
    not_one = 0

    for i in range(num):
        if edges[i] == 0:
            queue.append((i,0))
            if len(dag[i]) + scc_node[i] >= 1:
                not_one += 1
                if not_one > 1:
                    second = False

    #         print("i",i, dag[i], scc_node[i])
    # print("not", not_one)
    # print(queue)

    if len(queue) != 1:
        first = False

    while queue:
        cur,dep = queue.popleft()
        
        if level[dep]:
            first = False
        level[dep] += 1

        if len(dag[cur]) > 1:
            second = False

        if not first and not second:
            return

        for nxt in dag[cur]:
            edges[nxt] -= 1

            if not edges[nxt]:
                queue.append((nxt, dep+1))

    return


n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
edges_cnt = [0]*(n+1)
for _ in range(m):
    u,v = map(int,input().split())
    edges_cnt[u] += 1
    graph[u].append(v)

d = [-1]*(n+1)
visited = [False]*(n+1)
stk = []
idx = 0
num = 0
scc_idx = dict()
scc_node = dict()

for cur in range(1, n+1):
    if d[cur] == -1:
        dfs(cur)

dag = [[] for _ in range(num)]
edges = [0]*num

for cur in range(1, n+1):
    for nxt in graph[cur]:
        if scc_idx[cur] != scc_idx[nxt]:
            dag[scc_idx[cur]].append(scc_idx[nxt])
            edges[scc_idx[nxt]] += 1

# print(scc_node)
# print(scc_idx)
# print("dag",dag)
# print("edges",edges)
# print(dag_set)

# print("edgescnt", edges_cnt)

first = True
second = True

for i in range(num):
    if len(dag[i]) != len(set(dag[i])):
        second = False
        break
topology(dag, edges)

print(+first, +second, +first&second, sep='\n')

"""반례
3 3
1 1
3 3
3 3
"""