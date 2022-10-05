import sys, heapq
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a>b:
        parent[a] = b
    else:
        parent[b] = a



while True:
    m,n = map(int,input().split())
    parent = [i for i in range(m)]
    if m==0 and n==0:
        break
    graph = []
    ans = 0
    for _ in range(n):
        x,y,z = map(int,input().split())
        heapq.heappush(graph, [z,x,y])

    while graph:
        cost, x,y = heapq.heappop(graph)
        if find_parent(parent,x) != find_parent(parent, y):
            union_parent(parent, x,y)
        else:
            ans += cost

    print(ans)
