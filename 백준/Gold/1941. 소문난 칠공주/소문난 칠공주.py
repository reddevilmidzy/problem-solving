from itertools import combinations
import sys
input = sys.stdin.readline

dy = (1,0,-1,0)
dx = (0,1,0,-1)

def can_go(tmp):
    v = set()
    v.add((tmp[0]//5, tmp[0]%5))
    stk = [(tmp[0]//5, tmp[0]%5)]
    while stk:
        y,x = stk.pop()
        for j in range(4):
            ny,nx = y+dy[j], x+dx[j]
            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
            if (ny*5)+(nx) in tmp and (ny,nx) not in v:
                v.add((ny,nx))
                stk.append((ny,nx))

    return len(v) == 7

def solve(tmp):
    if not can_go(tmp):
        return 0
    s = 0
    for i in tmp:
        if board[i//n][i%n] == "S":
            s += 1
    return s >= 4

n = 5
m = 7
res = 0
board = [input().rstrip() for _ in range(n)]

for tmp in combinations(range(25), m):
    res += solve(tmp)

print(res)