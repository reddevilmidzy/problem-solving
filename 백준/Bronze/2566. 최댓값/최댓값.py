import sys
input = sys.stdin.readline

board = [list(map(int,input().split())) for _ in range(9)]
max_ans = -1
r,c = 0,0
for i in range(9):
    for j in range(9):
        if max_ans < board[i][j]:
            max_ans = board[i][j]
            r,c = i+1,j+1
print(max_ans)
print(r,c)