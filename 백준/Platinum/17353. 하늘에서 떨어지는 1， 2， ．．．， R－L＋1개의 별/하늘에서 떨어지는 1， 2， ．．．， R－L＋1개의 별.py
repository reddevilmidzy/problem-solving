import sys, math
input = sys.stdin.readline

def update_lazy(tree,lazy,node,start,end):
    if lazy[node] !=0:
        tree[node] += (end-start+1)*lazy[node]
        if start ^ end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def update_range(tree, lazy, node, start, end, left, right, diff):
    update_lazy(tree,lazy,node,start,end)
    if left > end or right < start:
        return 
    if left <= start and end <= right:
        tree[node] += (end-start+1)*diff
        if start ^ end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    
    update_range(tree,lazy,node*2,start,(start+end)//2,left,right,diff)
    update_range(tree,lazy,node*2+1,(start+end)//2+1,end,left,right,diff)
    tree[node] = tree[node*2] + tree[node*2+1]

def query(tree,lazy,node,start,end,left,right):
    update_lazy(tree,lazy,node,start,end)
    if left>end or right<start:
        return 0
    if left<= start and end <= right:
        return tree[node]
    lsum = query(tree,lazy,node*2,start,(start+end)//2,left,right)
    rsum = query(tree,lazy,node*2+1, (start+end)//2+1, end,left,right)
    return lsum + rsum

n = int(input())
arr = [0] + list(map(int,input().split()))
m = int(input())
h = math.ceil(math.log2(n))
tree_size = 1<<(h+1)

low_tree = [0]*tree_size
low_lazy = [0]*tree_size

high_tree = [0]*tree_size
high_lazy = [0]*tree_size
res = []
for _ in range(m):
    tmp = list(map(int,input().split()))
    if tmp[0]==1:
        a,b,c = tmp
        update_range(low_tree,low_lazy,1,1,n,b,c,1)
        update_range(high_tree,high_lazy,1,1,n,b,c,b-1)
    else:
        a,b = tmp
        u = arr[b]
        v = query(low_tree,low_lazy,1,1,n,b,b) * b
        w = query(high_tree,high_lazy,1,1,n,b,b) * -1
        res.append(u + v + w)
print(*res,sep='\n')