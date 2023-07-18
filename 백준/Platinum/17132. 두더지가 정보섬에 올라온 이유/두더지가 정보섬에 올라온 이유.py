# 최대값으로 연결
# 연결시 자식들 곱하기
import sys
input = sys.stdin.readline

def find(parent:list[int], x:int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent:list[int], a:int, b:int, w:int) -> None:
    if a < b:
        parent[b] = a
        child[a] += child[b]
        child[b] = child[a]
    else:
        parent[a] = b
        child[b] += child[a]
        child[a] = child[b]

n = int(input())
edges = [list(map(int,input().split())) for _ in range(n-1)]
edges.sort(key=lambda x:-x[2])
parent = [i for i in range(n+1)]
child = [1]*(n+1)
ans = 0

for x,y,w in edges:
    x = find(parent, x)
    y = find(parent, y)
    ans += (child[x]*child[y])*w
    union(parent, x, y, w)

print(ans)