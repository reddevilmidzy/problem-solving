import sys,math
input = sys.stdin.readline


# 트리 그리기
def init(a,tree,node,start,end):
    if start==end: # 리프노드라면
        tree[node] = a[start]

    else:
        init(a, tree,node*2, start, (start+end)//2) # 왼쪽 자식으로
        init(a, tree, node*2+1, (start+end)//2+1, end) # 오른쪽 자식으로
        tree[node] = tree[node*2] + tree[node*2+1]

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
    tree[node] = tree[node*2]+tree[node*2+1]


# 합구하기
# 목표지점까지 탐색 후 값을 가져옴
def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    # 왼쪽 합
    lsum = query(tree, node*2, start, (start+end)//2, left, right)
    # 오른쪽 합
    rsum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return lsum+rsum


n,m,k = map(int,input().split())
a = [int(input()) for _ in range(n)]
h = math.ceil(math.log2(n))

# 비트 연산자
tree_size = 1 << (h+1)
tree = [0]*tree_size

# 한번에 처리
m += k
init(a,tree,1,0,n-1)

for _ in range(m):
    what, t1, t2 = map(int,input().split())
    if what==1:
        index,val = t1, t2
        update(a, tree, 1, 0, n-1, index-1, val)
    else:
        left,right= t1, t2
        print(query(tree, 1, 0, n-1, left-1, right-1))