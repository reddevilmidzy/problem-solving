import sys, heapq
input = sys.stdin.readline

def distance(a, b):
    ax,ay,bx,by = a[0], a[1], b[0], b[1]
    return ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n,m = map(int,input().split())
pq = []
parent = [i for i in range(n+1)]
graph = [list(map(int,input().split())) for _ in range(n)]
ans = 0

for i in range(n-1):
    for j in range(i+1, n):
        heapq.heappush(pq, [distance(graph[i], graph[j]), i+1, j+1])

for _ in range(m):
    a,b, = map(int,input().split())
    union(parent, a, b)
    
while pq:
    dist, x, y = heapq.heappop(pq)
    if find(parent, x) != find(parent, y):
        union(parent, x, y)
        ans += dist

print(format(ans,".2f"))