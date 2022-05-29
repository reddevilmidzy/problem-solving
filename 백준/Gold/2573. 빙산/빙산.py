import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().rstrip().split())
ice = [list(map(int, input().rstrip().split())) for i in range(n)]
new = [[0 for i in range(m)] for i in range(n)]

def dfs(x,y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if ice[x][y] >0:
        ice[x][y] = 0
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1,y)
        dfs(x-1,y)
        return True
    return False
year = 0

while True:
    no = 0
    for i in range(n):
        for j in range(m):
            if ice[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
                        continue

                    if ice[nx][ny] == 0:
                        cnt += 1
                if ice[i][j] - cnt >= 0:
                    new[i][j] = ice[i][j] - cnt
                else:
                    new[i][j] = 0
            else:
                no += 1
    if no == n*m:
        print(0)
        break

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result += 1
    if result >= 2:
        print(year)
        break
    year += 1

    ice = new
    new = [[0 for i in range(m)] for i in range(n)]