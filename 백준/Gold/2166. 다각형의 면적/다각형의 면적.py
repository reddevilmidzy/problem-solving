import sys
input = sys.stdin.readline

def ccw(x1: int, x2: int, x3: int, y1: int, y2: int, y3: int) -> float:
    return ((x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1))/2

n = int(input())
lines = [list(map(int,input().split())) for _ in range(n)]
ans = 0

for i in range(1, n):
    ans += ccw(lines[0][0], lines[i-1][0], lines[i][0], lines[0][1], lines[i-1][1], lines[i][1])

print(abs(ans))