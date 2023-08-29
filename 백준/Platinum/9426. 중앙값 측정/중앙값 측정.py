import sys, math
input = sys.stdin.readline
INF = 65537

def update(node:int, st:int, ed:int, idx:int, val:int) -> None:
    if idx < st or idx > ed: return
    tree[node] += val
    if st == ed: return
    mid = (st + ed)//2
    update(2*node, st, mid, idx, val)
    update(2*node+1, mid+1, ed, idx, val)

def query(node:int, st:int, ed:int, idx:int) -> int:
    if st == ed: return st
    mid = (st + ed) //2
    if tree[2*node] >= idx: return query(2*node, st, mid, idx)
    return query(2*node+1, mid+1, ed, idx - tree[2*node])

n,k = map(int,input().split())
a = [int(input()) for _ in range(n)]
h = math.ceil(math.log2(INF))
tree = [0]*(1<<(h+1))
idx = (k+1)//2
ans = 0

for i in range(k):
    update(1, 0, INF, a[i], 1)

for i in range(k, n):
    ans += query(1, 0, INF, idx)
    update(1, 0, INF, a[i-k], -1)
    update(1, 0, INF, a[i], 1)

ans += query(1, 0, INF, idx)

print(ans)