from bisect import bisect_right
import sys, math
#sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def update(node:int, start:int, end:int, index:int, val:int) -> None:
    if index < start or index > end:
        return 
    
    tree[node].append(val)
    if start != end:
        update(node*2, start, (start+end)//2, index, val)
        update(node*2+1, (start+end)//2+1, end, index, val)

def query(node:int, start:int, end:int, left:int, right:int, val:int) -> int:
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return bisect_right(tree[node], val)
    
    return query(node*2, start, (start+end)//2, left, right, val) + query(node*2+1, (start+end)//2+1, end, left, right, val)

n,m = map(int,input().split())
a = list(map(int,input().split()))
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [[] for _ in range(tree_size)]
res = []

for i in range(1, n+1):
    update(1, 1, n, i, a[i-1])

for i in range(1, tree_size):
    tree[i].sort()

for _ in range(m):
    i,j,k = map(int,input().split())
    low = -int(1e9)
    high = int(1e9)

    while low <= high:
        mid = (low + high) // 2
        if query(1, 1, n, i, j, mid) < k:
            low = mid + 1
        else:
            high = mid - 1
    
    res.append(low)
print(*res,sep='\n')
