import sys, math
input = sys.stdin.readline

INF = int(1e9) + 1

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = [a[start], start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        if tree[node*2][0] <= tree[node*2+1][0]:
            tree[node] = [tree[node*2][0], tree[node*2][1]]
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
        tree[node] = [tree[node*2][0], tree[node*2][1]]
    else:
        tree[node] = [tree[node*2+1][0], tree[node*2+1][1]]

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return [INF, 0]
    if left <= start and end <= right:
        return [tree[node][0], tree[node][1]]

    l_min = query(tree, node*2, start, (start+end)//2, left, right)
    r_min = query(tree, node*2+1, (start+end)//2+1, end, left, right)

    if l_min[0] == INF:
        return r_min
    elif r_min[0] == INF:
        return l_min
    elif l_min[0] <= r_min[0]:
        return l_min
    else:
        return r_min

n = int(input())
a = list(map(int,input().split()))
m = int(input())
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [[0,0] for _ in range(tree_size)]

init(a, tree, 1, 0, n-1)

for _ in range(m):
    tmp = list(map(int,input().split()))

    if tmp[0] == 2:
        i,j = tmp[1], tmp[2]
        print(query(tree, 1,0,n-1, i-1, j-1)[1]+1)
    else:
        index, val = tmp[1], tmp[2]
        update(a, tree, 1, 0, n-1, index-1, val)