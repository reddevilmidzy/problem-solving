import sys,math
input = sys.stdin.readline


# 트리 그리기
def init(a,tree,node,start,end):
    if start==end: # 리프노드라면
        tree[node] = a[start]

    else:
        init(a, tree,node*2, start, (start+end)//2) # 왼쪽 자식으로
        init(a, tree, node*2+1, (start+end)//2+1, end) # 오른쪽 자식으로
        tree[node] = min(tree[node*2],tree[node*2+1]) # 최소값으로 부모 

# 수 변경위한 함수
def update(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return 
    if start==end:
        a[index] = val
        tree[node] = val
        return

    update(a, tree, node*2, start, (start+end)//2, index, val)
    update(a, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = min(tree[node*2],tree[node*2+1])


def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return -1

    if left <= start and end <= right:
        return tree[node]

    lmin = query(tree,node*2, start, (start+end)//2, left, right)
    rmin = query(tree, node*2+1, (start+end)//2 + 1, end, left, right)

    if lmin==-1:
        return rmin
    elif rmin ==-1:
        return lmin
    else:
        return min(lmin, rmin)


# n,m = map(int,input().split())
n = int(input())
a = list(map(int,input().split()))
h = math.ceil(math.log2(n))
m = int(input())

# 비트 연산자
tree_size = 1 << (h+1)
tree = [0]*tree_size


init(a,tree,1,0,n-1)

for _ in range(m):
    what, t1, t2 = map(int,input().split())
    if what==1:
        index,val = t1, t2
        update(a, tree, 1, 0, n-1, index-1, val)
    else:
        left,right= t1, t2
        print(query(tree, 1, 0, n-1, left-1, right-1))
#print(tree)