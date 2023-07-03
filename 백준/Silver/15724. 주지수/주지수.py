from sys import stdin
input = stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

pre_fix = [[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        pre_fix[i+1][j+1] = pre_fix[i][j+1] + pre_fix[i+1][j] + board[i][j] - pre_fix[i][j]

k = int(input())
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    print(pre_fix[x2][y2] - pre_fix[x2][y1-1] - pre_fix[x1-1][y2] + pre_fix[x1-1][y1-1])