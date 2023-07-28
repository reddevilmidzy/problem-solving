import sys, math
input = sys.stdin.readline
INF = 2*int(1e6)+1

def update(node:int, st:int, ed:int, idx:int, val:int) -> None:
    if idx < st or idx > ed: return
    tree[node] += val
    if st == ed: return
    mid = (st + ed)//2
    update(2*node, st, mid, idx, val)
    update(2*node+1, mid+1, ed, idx, val)

def query(node:int, st:int, ed:int, idx:int) -> int:
    tree[node] -= 1
    if st == ed: return st
    mid = (st + ed) //2
    if tree[2*node] >= idx: return query(2*node, st, mid, idx)
    return query(2*node+1, mid+1, ed, idx - tree[2*node])

n = int(input())
h = math.ceil(math.log2(INF*4))
tree = [0]*(1 << (h+1))

for _ in range(n):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        update(1, 0, INF, cmd[1], 1)
    else:
        print(query(1, 0, INF, cmd[1]))
