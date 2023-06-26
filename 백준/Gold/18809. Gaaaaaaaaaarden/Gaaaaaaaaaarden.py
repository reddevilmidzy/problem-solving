from itertools import combinations
from collections import deque
from sys import stdin
input = stdin.readline

dy = (1,0,-1,0)
dx = (0,1,0,-1)

# 배양액 뿌릴 녀석 고름
def bt(s:list[int]) -> None:
    if len(s) == g+r:
        global candies
        candies.append([pos[i] for i in s])
        return
    for i in range(len(pos)):
        if (s and s[-1] < i) or (not s):
            s.append(i)
            bt(s)
            s.pop()

def bfs(re_queue:deque, gr_queue:deque) -> int:  
    res = 0
    r_visited = [[0]*m for _ in range(n)]
    g_visited = [[0]*m for _ in range(n)]
    
    for y,x in re_queue:
        r_visited[y][x] = 1
    
    for y,x in gr_queue:
        g_visited[y][x] = 1

    while re_queue and gr_queue:

        r_new = []
        while re_queue:
            ry,rx = re_queue.popleft()
            for i in range(4):
                ny,nx = dy[i]+ry, dx[i]+rx
                if ny < 0 or nx < 0 or ny >= n or nx >= m: continue # 범위밖
                if board[ny][nx] == 0: continue

                # 아직 방문 안했거나, 다른 녀석이랑 만난다면
                if r_visited[ny][nx] == 0:
                    r_new.append((ny,nx))
                    r_visited[ny][nx] = r_visited[ry][rx]+1


        g_new = []
        while gr_queue:
            gy,gx = gr_queue.popleft()
            for i in range(4):
                ny,nx = dy[i]+gy, dx[i]+gx
                if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
                if board[ny][nx] == 0: continue

                if g_visited[ny][nx] == 0:
                    g_new.append((ny,nx))
                    g_visited[ny][nx] = g_visited[gy][gx]+1

        r_set = set(r_new)
        g_set = set(g_new)
        res += len(r_set & g_set) # 겹치는 부분

        re_queue = deque(list(r_set - g_set))
        gr_queue = deque(list(g_set - r_set))

    return res

def make():
    bt([])
    for candy in candies:
        cc = set(candy)
        for x in combinations(candy, g):
            gg = set(x)
            rr = cc - gg
            gr_queue = deque([*gg])
            re_queue = deque([*rr])
            ans.append(bfs(re_queue, gr_queue))

n,m,g,r = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
# 0: 호수, 1: 배양액 X, 2: 배양액 O

pos = []
ans = []
candies = []
sepa = []
for y in range(n):
    for x in range(m):
        if board[y][x] == 2:
            pos.append((y,x))

make()
print(max(ans))