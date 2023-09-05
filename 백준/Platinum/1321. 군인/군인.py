import sys, math
input = sys.stdin.readline

def init(a:list[int], tree:list[int], node:int, st:int, ed:int) -> None:
    if st == ed:
        tree[node] = a[st]
    else:
        mid = (st+ed)//2
        init(a, tree, node*2, st, mid)
        init(a, tree, node*2+1, mid+1, ed)
        tree[node] = tree[node*2]+tree[node*2+1]

def update(node:int, st:int, ed:int, idx:int, val:int) -> None:
    if idx < st or idx > ed: return
    tree[node] += val
    if st == ed: return
    mid = (st + ed)//2
    update(2*node, st, mid, idx, val)
    update(2*node+1, mid+1, ed, idx, val)


def query(node:int, st:int, ed:int, idx:int) -> int:
    if st == ed: return st
    mid = (st+ed)//2
    if tree[2*node] >= idx:
        return query(2*node, st, mid, idx)
    return query(2*node+1, mid+1, ed, idx-tree[2*node])

n = int(input())
h = math.ceil(math.log2(n))
tree = [0]*(1<<(h+1))
a = list(map(int,input().split()))
init(a,tree,1,0,n-1)
# print(tree)
m = int(input())
for _ in range(m):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        update(1, 0, n-1, cmd[1]-1, cmd[2])
    else:
        print(query(1, 0, n-1, cmd[1])+1)