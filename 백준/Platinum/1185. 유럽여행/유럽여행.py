# 간선은 정확이 두번 사용
# 정점은 두번이상
import sys, heapq
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

def solve():
    n,p = map(int,input().split())
    parent = [i for i in range(n+1)]
    cost = [0] + [int(input()) for _ in range(n)]
    edges = [list(map(int,input().split())) for _ in range(p)]
    edges.sort(key=lambda x:2*x[2]+cost[x[0]]+cost[x[1]])
    ans = min(cost[1:])
    mst = 0

    for u,v,w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            ans += 2*w+cost[u]+cost[v]
            mst += 1
            if mst == n-1: break
    return ans
if __name__ == "__main__":
    print(solve())