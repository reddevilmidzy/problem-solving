from math import ceil, log2
from sys import stdin
input = stdin.readline

def init(tree, node, start, end):
    if start == end:
        tree[node] = 1
    else:
        init(tree, node*2, start, (start+end)//2)
        init(tree, node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] | tree[node*2+1]


def update_lazy(tree, lazy, node, start, end):
    if lazy[node] == 0: return
    tree[node] = lazy[node]
    if start != end:
        lazy[node*2] = lazy[node]
        lazy[node*2+1] = lazy[node]
    lazy[node] = 0

def update_range(tree, lazy, node, start, end, left, right, val):
    update_lazy(tree, lazy, node, start, end)
    if left > end or right < start:
        return
    if left <= start and end <= right:
        lazy[node] = val
        update_lazy(tree, lazy, node, start, end)
        return

    update_range(tree,lazy,node*2,start,(start+end)//2,left,right,val)
    update_range(tree,lazy,node*2+1,(start+end)//2+1,end,left,right,val)
    tree[node] = tree[node*2] | tree[node*2+1]

def query(tree,lazy,node,start,end,left,right):
    update_lazy(tree,lazy,node,start,end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree,lazy,node*2,start,(start+end)//2,left,right)
    rsum = query(tree,lazy,node*2+1,(start+end)//2+1,end,left,right)
    return lsum | rsum

n,t,q = map(int,input().split())
h = ceil(log2(n))
tree_size = 1<<(h+1)
tree = [0]*tree_size
lazy = [0]*tree_size

init(tree, 1, 0, n-1)


for _ in range(q):
    cmd = list(input().rstrip().split())
    if cmd[0] == "Q":
        x,y = int(cmd[1]), int(cmd[2])
        res = query(tree, lazy, 1, 0, n-1, min(x,y)-1, max(x,y)-1)
        ans = 0
        while res:
            ans += res&1
            res >>=1
        print(ans)
    else:
        x,y,z = int(cmd[1]), int(cmd[2]), int(cmd[3])
        update_range(tree, lazy, 1, 0, n-1, min(x,y)-1, max(x,y)-1, (1 << (z -1)))
