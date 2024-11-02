import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(parent: list[int], x: int) -> int:
    if parent[x] != x:
        y = find(parent, parent[x])
        weight[x] += weight[parent[x]]
        parent[x] = y
    return parent[x]

def union(parent: list[int], a: int, b: int, w: int) -> None:
    pa = find(parent, a)
    pb = find(parent, b)
    
    if pa != pb:
        weight[pb] = (-weight[b]) + weight[a] + w
        parent[pb] = pa

res = []
while True:
    n,m = map(int,input().split())
    if n==0: break
    parent = [i for i in range(n + 1)]
    weight = [0] * (n + 1)
    for _ in range(m):
        cmd = list(input().rstrip().split())

        if cmd[0] == "!": # 업데이트
            a,b,w = map(int, cmd[1:])
            union(parent, a, b, w)
        else:
            u,v = map(int, cmd[1:])
            if find(parent, u) != find(parent, v):
                res.append("UNKNOWN")
            else:
                res.append(weight[v] - weight[u])
print(*res,sep='\n')
