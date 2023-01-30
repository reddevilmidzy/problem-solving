import sys, heapq
input = sys.stdin.readline

def solve(integer: int, graph: list, board: list) -> int:
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] != board[i][j]:
                return -1

    return integer

INF = int(1e9)
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
board = [[INF]*n for _ in range(n)]
for x in range(n):
    board[x][x] = 0
edges = []
for i in range(n):
    for j in range(i+1, n):
        # print(i,j)
        heapq.heappush(edges,[graph[i][j], i,j])
ans = 0
while edges:
    cost,a,b = heapq.heappop(edges)
    if cost < board[a][b]:
        ans += cost
        board[a][b] = cost
        board[b][a] = cost
    if cost < board[b][a]:
        ans += cost
        board[a][b] = cost
        board[b][a] = cost

    for x in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                if board[i][j] > board[i][x] + board[x][j]:
                    board[i][j] = board[i][x] + board[x][j]
                    board[j][i] = board[i][x] + board[x][j]

print(solve(ans, graph, board))