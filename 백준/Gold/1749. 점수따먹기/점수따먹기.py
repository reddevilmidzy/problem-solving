import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

pre_fix = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        pre_fix[i][j] = pre_fix[i-1][j] + pre_fix[i][j-1] - pre_fix[i-1][j-1] + a[i-1][j-1]

ans = -int(1e4)

for r in range(1, n+1):
    for c in range(1, m+1):
        for y in range(r, n+1):
            for x in range(c, m+1):
                tmp = pre_fix[y][x] - pre_fix[y][c-1] - pre_fix[r-1][x] + pre_fix[r-1][c-1]
                if ans < tmp:
                    ans = tmp
print(ans)