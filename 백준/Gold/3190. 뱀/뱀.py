import sys
from collections import deque
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [-1,0,1,0]
def direc_change(d,c):
    if c == 'L':
        d = (d-1)%4
    else:
        d = (d+1)%4
    return d

n = int(input())
k = int(input())
board = [[0]*n for _ in range(n)]
for i in range(k):
    a,b = map(int,input().rstrip().split())
    board[a-1][b-1] = 1

l = int(input())
times = {}
for j in range(l):
    x,c = input().rstrip().split()
    times[int(x)] = c

direc = 1
time = 1
y,x = 0,0
snake = deque([[y,x]])
board[y][x] = 2

while True:
    y,x = y + dy[direc], x + dx[direc] # 현재 이동 방향대로
    if 0 <= y < n and 0 <= x < n and board[y][x] != 2: # board==2 는 뱀이 존재하는 곳
        if not board[y][x] == 1: # 사과가 없다면
            dely,delx = snake.popleft()
            board[dely][delx] = 0
        board[y][x] = 2
        snake.append([y,x])
        if time in times.keys(): # 방향 변환
            direc = direc_change(direc, times[time])
        time += 1
    else:
        break
print(time)