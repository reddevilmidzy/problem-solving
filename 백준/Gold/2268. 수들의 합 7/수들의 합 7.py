import sys, math
input = sys.stdin.readline

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree,node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2]+tree[node*2+1]
    

def update(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node] = val
        return
    update(a, tree, node*2, start, (start+end)//2, index,val)
    update(a, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = tree[node*2] + tree[node*2+1]


def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree, node*2, start, (start+end)//2, left,right)
    rsum = query(tree,node*2+1, (start+end)//2+1, end, left, right)
    return lsum+rsum


n,m = map(int,input().split())
a = [0 for _ in range(n)]
#print(a)
h = math.ceil(math.log2(n))

tree_size = 1 << (h+1)
tree = [0]*tree_size
#print(tree)
init(a, tree, 1, 0, n-1)

for _ in range(m):
    what, t1,t2 = map(int,input().split())
    if what==0:
        left, right = min(t1, t2), max(t1, t2)
        print(query(tree, 1, 0, n-1, left-1, right-1))
    else:
        index, val = t1, t2
        update(a, tree, 1, 0, n-1, index-1, val)