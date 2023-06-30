from sys import stdin
input = stdin.readline

def find(x:int, parent:list[int]) -> int:
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a:int, b:int, parent:list[int]) -> None:
    a = find(a, parent)
    b = find(b, parent)

    if a < b:
        parent[b] = a
        cost[a] += cost[b]
    elif a > b:
        parent[a] = b
        cost[b] += cost[a]

n,m,q = map(int,input().split())
graph = [[] for _ in range(n+1)]
tree = []
edges = [tuple(map(int,input().split())) for _ in range(m)]

tmp = [False]*m
cut = []

for _ in range(q):
    k = int(input())-1
    cut.append(k)
    tmp[k] = True

for i in range(m):
    if not tmp[i]:
        tree.append(edges[i])

parent = [i for i in range(n+1)]
cost = [1 for _ in range(n+1)]

for x,y in tree:
    if find(x, parent) != find(y, parent):
        union(x,y,parent)

ans = 0

for i in range(q-1, -1, -1):
    x,y = edges[cut[i]]
    if find(x, parent) != find(y, parent): # 둘의 부모가 다르다면 이건 이어졌던것
        ans += cost[find(x, parent)] * cost[find(y, parent)]
        union(x,y,parent)

print(ans)