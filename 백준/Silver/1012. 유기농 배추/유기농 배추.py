import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)

def dfs(x,y):
    if x <= -1 or x >=n or y <= -1 or y >= m:
        return False
    if bat[x][y] == 1:
        bat[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

for i in range(int(input().rstrip())):
    m, n, k = map(int, input().rstrip().split())
    bat = [[0 for u in range(m)] for o in range(n)]
    for j in range(k):
        x, y = map(int, input().rstrip().split())
        bat[y][x] = 1
    result = 0
    for q in range(n):
        for w in range(m):
            if dfs(q,w)== True:
                result += 1
    print(result)