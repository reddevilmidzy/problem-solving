import sys, math
input = sys.stdin.readline

def init(a, tree, node, start, end, small):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2 , small)
        init(a, tree, node*2+1, (start+end)//2+1, end, small)

        if small:
            tree[node] = min(tree[node*2], tree[node*2+1])
        else:
            tree[node] = max(tree[node*2], tree[node*2+1])

def query(tree, node, start, end, left, right, small):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]

    lmin = query(tree, node*2, start, (start+end)//2, left, right, small)
    rmin = query(tree, node*2+1, (start+end)//2+1, end, left, right, small)

    if lmin==-1:
        return rmin
    elif rmin==-1:
        return lmin
    else:
        if small:
            return min(lmin, rmin)
        else:
            return max(lmin, rmin)

n,q = map(int,input().split())
a = [int(input()) for _ in range(n)]
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
max_tree = [0]*tree_size
min_tree = [0]*tree_size

init(a, min_tree, 1, 0, n-1, True)
init(a, max_tree, 1, 0, n-1, False)

for _ in range(q):
    x,y = map(int,input().split())
    print(query(max_tree, 1, 0, n-1, x-1, y-1, False) - query(min_tree, 1, 0, n-1, x-1, y-1, True))