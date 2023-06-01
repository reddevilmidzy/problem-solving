from collections import deque
import sys
input = sys.stdin.readline

dy = (0,-1,0,1)
dx = (1,0,-1,0)

def out_of_range(ny:int, nx:int) -> bool:
    return ny < 0 or nx < 0 or ny >= n or nx >= m

def bfs(r:int, c:int) -> int:
    res = 0
    queue = deque()
    queue.append((r,c))

    if board[r][c] == "$":
        res += 1
        board[r][c] = "."
    elif board[r][c].islower():
        keys.add(board[r][c])
        board[r][c] = "."
    elif board[r][c].isupper():
        if board[r][c].lower() not in keys: # 초판부터 장난질이냐
            return 0
        else:
            board[r][c] = "."
    visited[r][c] = True
    
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny,nx = dy[i]+y, dx[i]+x
            if out_of_range(ny,nx): continue
            if visited[ny][nx]: continue
            if board[ny][nx] == "*": continue

            if board[ny][nx] == "$":
                res += 1
                board[ny][nx] = "."
                visited[ny][nx] = True
                queue.append((ny,nx))
            elif board[ny][nx].islower():        # 키가 있음
                keys.add(board[ny][nx])
                board[ny][nx] = "."
                visited[ny][nx] = True
                queue.append((ny,nx))
            elif board[ny][nx].isupper():
                if board[ny][nx].lower() in keys:
                    board[ny][nx] = "."
                    visited[ny][nx] = True
                    queue.append((ny,nx))
            else:
                visited[ny][nx] = True
                queue.append((ny,nx))

    return res # 이번 탐색에서 찾은 문서 개수

def add_action(y:int, x:int) -> None:
    st_pos.append((y,x))
    visited[y][x] = True


t = int(input())
for _ in range(t):
    # print("="*10)
    n,m = map(int,input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    keys = set(input().rstrip())
    ans = 0
    if keys == '0': keys.clear()                # 가진 키 없으면 비우기

    st_pos = []
    visited = [[False]*m for _ in range(n)]

    for y in range(n):
        if board[y][0] != "*":                  # 사이드가 벽이 아니라면
            add_action(y,0)
        if board[y][m-1] != "*":
            add_action(y,m-1)

    for x in range(1, m-1):                     # 세로랑 겹칠 거 같
        if board[0][x] != "*":
            add_action(0,x)
        if board[n-1][x] != "*":
            add_action(n-1,x)

    while True:
        tmp = 0
        visited = [[False]*m for _ in range(n)]
        key_len = len(keys)
        for r,c in st_pos:
            tmp += bfs(r,c)
        if not tmp and key_len == len(keys):
            break
        ans += tmp
    print(ans)