import sys, heapq
input = sys.stdin.readline

def find(parent: list[int], x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent: list[int], i: int, j: int) -> None:
    i = find(parent, i)
    j = find(parent, j)
    if i < j:
        parent[j] = i
    else:
        parent[i] = j

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]

hq = []
parent = [i for i in range(n)]
tree = [0]*n

for i in range(n):
    for j in range(i+1, n):
        if board[i][j] == "Y":
            heapq.heappush(hq, (i,j))

if len(hq) < m: print(-1); exit(0)

tot = 0
candy = []
while hq:
    i, j = heapq.heappop(hq)
    # 연결 안됨
    if find(parent, i) != find(parent, j):
        union(parent, i, j)
        tree[i] += 1
        tree[j] += 1
        tot += 1

    # 연결 됐지만 우선순위 높기에 후보군에 오름
    # mst 완성 후 도로 갯수 부족할 때 쓸 녀석
    else:
        heapq.heappush(candy, (i,j))

# mst 못 만듬
if tot < n - 1: print(-1); exit(0)

while tot < m:
    i,j = heapq.heappop(candy)
    tree[i] += 1
    tree[j] += 1
    tot += 1

print(*tree)