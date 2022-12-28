import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

pre_fix = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        pre_fix[i][j] = pre_fix[i-1][j] + pre_fix[i][j-1] + board[i-1][j-1] - pre_fix[i-1][j-1]


k = int(input())
for _ in range(k):
    i,j,x,y = map(int,input().split())
    print(board[i-1][j-1] if i==x and j==y else pre_fix[x][y] - pre_fix[i-1][y] - pre_fix[x][j-1] + pre_fix[i-1][j-1])