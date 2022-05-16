from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    field[x][y] = 0
    q = deque()
    q.append([x, y])
    
    while q:
        a, b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
                field[nx][ny] = 0
                q.append([nx, ny])

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    field = []
    count = 0
    for _ in range(h):
        field.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if field[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)