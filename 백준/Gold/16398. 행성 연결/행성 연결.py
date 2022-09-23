import heapq, sys
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
    
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dist = []
edges = 0
parent = [i for i in range(n)]
for i in range(n):
    for j in range(i):
        heapq.heappush(dist, (graph[i][j], i, j))
ans = 0
if n == 1:
    print(0)
else:
    while dist:
        cost, a, b = heapq.heappop(dist)
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            ans += cost
            edges += 1
        if edges == n-1:
            print(ans)
            break

# print(ans)