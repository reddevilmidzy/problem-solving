import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]

res = 0

for i in range(n):
    pre = False
    for j in range(m):
        if board[i][j] == "-":
            if not pre:
                pre = True
                res += 1
        else:
            pre = False

for j in range(m):
    pre = False
    for i in range(n):
        if board[i][j] == "|":
            if not pre:
                pre = True
                res += 1
        else:
            pre = False

print(res)
