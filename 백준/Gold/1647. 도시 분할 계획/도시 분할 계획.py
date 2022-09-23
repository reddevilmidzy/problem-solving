import heapq,sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]
dag = []
cost = []
edges = 0
for _ in range(m):
    u,v,w = map(int,input().split())
    heapq.heappush(dag, [w,u,v])

while dag:
    c,a,b = heapq.heappop(dag)

    if find_parent(parent,a) != find_parent(parent,b):
        cost.append(c)
        union_parent(parent,a,b)
        edges += 1

    if edges==n-1:
        break

print(sum(cost)-max(cost))
