import sys, math
input = sys.stdin.readline

def init(a,tree,node,start,end):
    if start==end:
        tree[node] = a[start]
    else:
        init(a,tree,node*2,start,(start+end)//2)
        init(a,tree,node*2+1,(start+end)//2+1,end)
        tree[node] = tree[node*2]+tree[node*2+1]


def update_lazy(tree,lazy,node,start,end):
    if lazy[node] !=0: # lazy하게 나중에 하겠다고 한게 있다면
        tree[node] += (end-start+1)*lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0 # 다 더했으니 지워주자

def update_range(tree, lazy, node, start, end, left, right, diff):
    update_lazy(tree,lazy,node,start,end)
    if left > end or right < start:
        return 
    if left <= start and end <= right:
        tree[node] += (end-start+1)*diff
        if start != end:
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
arr = list(map(int,input().split()))
m = int(input())
h = math.ceil(math.log2(n))
tree_size = 1<<(h+1)
tree = [0]*tree_size
lazy = [0]*tree_size

init(arr,tree,1,0,n-1)

for _ in range(m):
    tmp = list(map(int,input().split()))
    if tmp[0]==1:
        a,b,c,d = tmp
        update_range(tree,lazy,1,0,n-1,b-1,c-1,d)
    else:
        a,b = tmp
        print(query(tree,lazy,1,0,n-1,b-1,b-1))
