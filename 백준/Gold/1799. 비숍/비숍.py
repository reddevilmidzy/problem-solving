import sys
input = sys.stdin.readline

def color(r:int, c:int, visited:list[list[bool]], t:int) -> None:

    visited[r][c] += t
    ny,nx = r+1,c+1
    while ny < n and nx < n:
        visited[ny][nx] += t
        ny += 1
        nx += 1    
    ny,nx = r+1,c-1
    while ny < n and nx >= 0:
        visited[ny][nx] += t
        ny += 1
        nx -= 1


def bt(s:list[int], visited:list[list[bool]], candy:list[tuple[int]], m:int, is_white: bool) -> None:
    if is_white:
        global white_ans
        white_ans = max(white_ans, len(s))
    else:
        global black_ans
        black_ans = max(black_ans, len(s))

    for i in range(m):
        r,c = candy[i]
        if not visited[r][c] and (not s or (s and s[-1] < i)):
            color(r,c,visited,1)
            s.append(i)
            bt(s,visited, candy, m, is_white)
            s.pop()
            color(r,c,visited,-1) # 지우기

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

white = []
black = []
white_ans = 0
black_ans = 0

for r in range(n):
    for c in range(n):
        if board[r][c] == 1: # 놓을 수 있는 곳
            if r%2 == c%2:
                white.append((r,c))
            else:
                black.append((r,c))

bt([], visited, black, len(black), False)
bt([], visited, white, len(white), True)

print(black_ans + white_ans)