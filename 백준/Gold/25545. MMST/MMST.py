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


def solve():
    if n-1 == m: return False
    use = {i:False for i in range(1, m+1)}

    # mst
    parent = [i for i in range(n+1)]
    for idx, u, v, w in hq:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            use[idx] = True

    # mmst
    parent = [i for i in range(n+1)]

    # mst 포함 아닌 아무거나 추가
    for idx, u, v, w in hq:
        if not use[idx]:
            union(parent, u, v)
            edges.append(idx)
            break

    for idx, u, v, w in hq:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            edges.append(idx)

            if len(edges) == n-1:
                break

    return True

n,m = map(int,input().split())
# idx, u, v, w
hq = [(i, *map(int,input().split())) for i in range(1,m+1)]
hq.sort(key=lambda x:x[-1])
edges = []
if solve():
    print("YES")    
    print(*edges)
else:
    print("NO")