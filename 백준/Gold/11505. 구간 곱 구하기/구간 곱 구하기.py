import sys,math
input = sys.stdin.readline
DIV = 10**9+7
def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = (tree[node*2]*tree[node*2+1])%DIV


def update(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node] = val
        return

    update(a, tree,node*2, start,(start+end)//2, index, val)
    update(a, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = (tree[node*2]*tree[node*2+1])%DIV


def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return -1

    if left <= start and end <=right:
        return tree[node]
    
    ltimes = query(tree, node*2, start, (start+end)//2, left, right)
    rtimes = query(tree, node*2+1, (start+end)//2+1, end, left, right)

    if ltimes==-1:
        return rtimes
    elif rtimes==-1:
        return ltimes
    else:
        return (rtimes*ltimes)%DIV

n,m,k = map(int,input().split())
a = [int(input()) for _ in range(n)]
h = math.ceil(math.log2(n))

tree_size = 1 << (h+1)
tree = [0]*tree_size
init(a, tree, 1, 0, n-1)


for _ in range(m+k):
    what, t1,t2 = map(int,input().split())
    if what==1:
        index,val = t1,t2
        update(a,tree,1,0,n-1,index-1,val)
    else:
        left,right = t1,t2
        print(query(tree,1,0,n-1,left-1,right-1))