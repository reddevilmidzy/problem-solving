import sys, math
input = sys.stdin.readline

def init(a, tree, node, start, end):
    if start==end:
        tree[node] = [a[start], start]
    
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        if tree[node*2][0] <= tree[node*2+1][0]:
            tree[node]= [tree[node*2][0], tree[node*2][1]]
        else:
            tree[node] = [tree[node*2+1][0], tree[node*2+1][1]]


def update(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node] = [val, index]
        return
    update(a, tree, node*2, start, (start+end)//2, index, val)
    update(a, tree, node*2+1, (start+end)//2+1, end, index, val)
    
    if tree[node*2][0] <= tree[node*2+1][0]:
        tree[node]= [tree[node*2][0], tree[node*2][1]]
    else:
        tree[node] = [tree[node*2+1][0], tree[node*2+1][1]]

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return -1

    if left <= start and end <= right:
        return tree[node][1]+1
    
    lmin = query(tree, node*2, start, (start+end)//2, left, right)
    rmin = query(tree, node*2+1, (start+end)//2+1, end, left, right)

n= int(input())
a = list(map(int,input().split()))
m = int(input())
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [[0,0] for _ in range(tree_size)]

init(a, tree, 1, 0, n-1)

for _ in range(m):
    tmp = list(map(int,input().split()))
    if tmp[0]==2:
        print(query(tree, 1, 0, n-1, 0, n-1))
    else:
        index, val = tmp[1], tmp[2]
        update(a, tree, 1, 0, n-1, index-1, val)