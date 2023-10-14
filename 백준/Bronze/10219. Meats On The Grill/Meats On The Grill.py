import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h,w = map(int,input().split())
    board = [input().rstrip() for _ in range(h)]
    for i in range(h-1,-1,-1):
        print(board[i])