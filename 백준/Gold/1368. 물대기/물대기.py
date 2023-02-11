import sys,heapq
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a>b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
hq = []
for i in range(1, n+1): heapq.heappush(hq, (int(input()), i, 0))

graph = [list(map(int,input().split())) for _ in range(n)]
parent = [i for i in range(n+1)]
ans = 0
edges = n

for i in range(n):
    for j in range(i+1,n):
        heapq.heappush(hq,(graph[i][j],i+1,j+1))

while hq:
    cost, i,j = heapq.heappop(hq)
    if find_parent(parent, i) != find_parent(parent, j):
        union_parent(parent, i, j)
        ans += cost
        edges -= 1
        
        if not edges:
            break

print(ans)