import sys
input = sys.stdin.readline

def find(parent:list[int], x:int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent:list[int], a:int, b:int) -> None:
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
graph = [[0]*n for _ in range(n)]
parent = [i for i in range(n)]
pre = 0
edges = []

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(i+1, n):
        if tmp[j] < 0:
            pre -= tmp[j]
            union(parent, i, j)

        else:
            edges.append((tmp[j], i, j))

edges.sort()
ans = []
new = 0

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        ans.append((a+1,b+1))
        new += cost


print(new + pre, len(ans))
for i in ans:
    print(*i)