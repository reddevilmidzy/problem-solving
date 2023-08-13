import sys, math
input = sys.stdin.readline

def init(a,tree,node,st,ed):
    if st == ed:
        tree[node] = a[st]
    else:
        init(a,tree,node*2,st,(st+ed)//2)
        init(a,tree,node*2+1,(st+ed)//2+1,ed)
        tree[node] = max(tree[node*2], tree[node*2+1])

def query(tree,node,st,ed,left,right):
    if left > ed or right < st:
        return -1
    if left <= st and ed <= right:
        return tree[node]
    
    lmax = query(tree,node*2,st,(st+ed)//2,left,right)
    rmax = query(tree,node*2+1,(st+ed)//2+1,ed,left,right)

    return max(lmax, rmax)

n,m = map(int,input().split())
a = list(map(int,input().split()))
h = math.ceil(math.log2(n))

tree_size = 1 << (h+1)
tree = [0]*tree_size

init(a,tree,1,0,n-1)

for i in range(m-1, n-m+1):
    print(query(tree,1,0,n-1,i-m+1, i+m-1), end=' ')