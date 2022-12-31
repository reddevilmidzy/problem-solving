import sys, heapq
input = sys.stdin.readline

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

n = int(input())
sky = [list(map(float, input().split()))+[i] for i in range(n)]
edges = []

for i in range(n-1):
    for j in range(i+1,n):
        pre_x, pre_y, pre_node = sky[i][0], sky[i][1], sky[i][2]
        post_x, post_y, post_node = sky[j][0], sky[j][1], sky[j][2]
        dist = (abs(pre_x-post_x)**2 + abs(pre_y-post_y)**2)**0.5
        heapq.heappush(edges, [dist, pre_node, post_node])

ans = 0
parent = [i for i in range(n)]
while edges:
    dist, a, b = heapq.heappop(edges)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        ans += dist
print(ans)