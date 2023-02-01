import sys
input = sys.stdin.readline

n = int(input())
board = [[0]*100 for _ in range(100)]
ans = 0
for _ in range(n):
    a,b = map(int,input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            board[i][j] = 1

print(sum(map(sum,board)))