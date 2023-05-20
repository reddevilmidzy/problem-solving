import sys
input = sys.stdin.readline

def dfs(r:int, c:int, way:int, t:int, idx:int, visited: list[list[int]]):
    if r < 0 or c < 0 or r >= n or c >= m: return
    if board[r][c] == 6: return
    visited[r][c] = 0
    dfs(r+d[t][way][idx][0], c+d[t][way][idx][1], way, t, idx, visited)

def bt(s: list[int], idx: int):
    if len(s) == k:
        visited = [[1]*m for _ in range(n)]
        for i in range(k):
            for j in range(len(d[cctv_type[i]][s[i]])):
                dfs(cctv[i][0], cctv[i][1], s[i], cctv_type[i], j, visited)

        ans.append(sum(map(sum, visited)))
        return
    
    for i in range(len(d[cctv_type[idx]])):
        s.append(i)
        bt(s, idx+1)
        s.pop()

d = {1: [[(0,-1)], [(1,0)], [(0,1)], [(-1,0)]], 
     2: [[(1,0), (-1,0)], [(0,1), (0,-1)]],
     3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(0,-1), (1, 0)], [(0, -1), (-1, 0)]],
     4: [[(-1, 0), (0, 1), (1, 0)], [(0,1), (1, 0), (0, -1)], [(0,-1), (1, 0), (-1, 0)], [(0, -1), (-1, 0), (0, 1)]],
     5: [[(-1, 0), (0, 1), (1, 0), (0, -1)]]}

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

cctv = []
cctv_type = []
wall = 0
ans = []

for i in range(n):
    for j in range(m):
        if 0 < board[i][j] < 6:
            cctv.append((i,j))
            cctv_type.append((board[i][j]))
        elif board[i][j] == 6:
            wall += 1

k = len(cctv) # cctv 개수

bt([], 0)

print(min(ans) - wall)