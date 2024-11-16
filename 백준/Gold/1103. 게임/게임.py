import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = (0, 1, -1, 0)
dx = (1, 0, 0, -1)

n,m = map(int,input().split())
board = [list(map(int,input().rstrip().replace('H', '0'))) for _ in range(n)]

dp = [[1]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
flag = False

def solve(y: int, x: int) -> int:
    global flag
    if dp[y][x] != 1:
        return dp[y][x]

    for k in range(4):
        ny, nx = y + dy[k] * board[y][x], x + dx[k] * board[y][x]
        if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
        if not board[ny][nx]: continue

        if not visited[ny][nx]:
            visited[ny][nx] = True
            dp[y][x] = max(dp[y][x], solve(ny, nx) + 1)
            visited[ny][nx] = False
        else:
            print(-1)
            exit()

    return dp[y][x]

print(solve(0,0))
