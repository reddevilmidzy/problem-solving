import sys, math
input = sys.stdin.readline

def init(a: list[int], tree: list[int], node: int, st: int, ed: int) -> None:
    if st == ed:
        tree[node] = a[st]
    else:
        init(a, tree, node*2, st, (st+ed)//2)
        init(a, tree, node*2+1, (st+ed)//2+1, ed)
        tree[node] = tree[node*2] + tree[node*2+1]


def update(a: list[int], tree: list[int], node: int, st: int, ed: int, idx: int, val: int) -> None:
    if idx < st or idx > ed:
        return
    if st == ed:
        a[idx] += val
        tree[node] += val
        return
    update(a, tree, node*2, st, (st+ed)//2, idx, val)
    update(a, tree, node*2+1, (st+ed)//2+1, ed, idx, val)
    tree[node] = tree[node*2] + tree[node*2+1]

def query(tree: list[int], node: int, st: int, ed: int, left: int, right: int) -> int:
    if left > ed or right < st:
        return 0
    if left <= st and ed <= right:
        return tree[node]
    
    lsum = query(tree, node*2, st, (st+ed)//2, left, right)
    rsum = query(tree, node*2+1, (st+ed)//2+1, ed, left, right)
    return lsum + rsum


n,q = map(int,input().split())
a = [0]*(n+1)
h = math.ceil(math.log2(n+1))

tree_size = 1 << (h+1)
tree = [0]*tree_size

init(a, tree, 1, 0, n)

for _ in range(q):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        p,x = cmd[1:]
        update(a, tree, 1, 0, n, p, x)
    else:
        p,q = cmd[1:]
        print(query(tree, 1, 0, n, p, q))
