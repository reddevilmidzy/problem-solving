import heapq, sys
input =  sys.stdin.readline

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

INF = int(1e9)
n = int(input())
graph = [[] for _ in range(n+1)]
edges = []
parent = [i for i in range(n+1)]
for i in range(1,n):
    tmp = list(map(int,input().split()))
    for j in range(i+1,n+1):
        heapq.heappush(edges, [tmp[j-i-1], i, j])

edge = n-1
while edges:
    cost, a,b = heapq.heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a,b)
        graph[a].append(b)
        graph[b].append(a)
        edge -=1
    if edge==0:
        break

for i in graph[1:]:
    print(len(i), *sorted(i))