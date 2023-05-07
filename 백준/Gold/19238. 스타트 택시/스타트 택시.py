from collections import deque
import sys
input = sys.stdin.readline

dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)

def minus(num: int) -> int:
    return num - 1

def bfs(st_y:int, st_x:int, target: set) -> None:
    queue = deque()
    queue.append((st_y,st_x,0))
    visited = [[False]*n for _ in range(n)]
    visited[st_y][st_x] = True

    max_cnt = int(1e9)
    tmp = []

    while queue:
        y,x,cnt = queue.popleft()

        if max_cnt < cnt: # 최대 넘음
            continue
        if (y, x) in target and cnt <= max_cnt:
            max_cnt = cnt
            tmp.append((cnt, y, x))
            continue
        for i in range(4):
            ny,nx = dy[i]+y, dx[i]+x
            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue

            if board[ny][nx] == 0 and not visited[ny][nx]:
                queue.append((ny,nx,cnt+1))
                visited[ny][nx] = True

    if not tmp:
        return -1,-1,-1 # 이동 불가
    tmp.sort()
    return tmp[0][0], tmp[0][1], tmp[0][2]
n,m,fuel = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
# r,c = map(minus, map(int,input().split()))
r,c = map(int,input().split())
r,c = r-1, c-1
customers = dict()

for i in range(m):
    t,u,v,w = map(int,input().split())
    t,u,v,w = t-1,u-1,v-1,w-1
    customers[i] = [t,u,v,w]

for _ in range(m): # 고객
    postion = dict() # 위치
    target = set()
    
    for key, val in customers.items():
        st_y,st_x,ed_y,ed_x = val
        target.add((st_y, st_x))
        postion[(st_y, st_x)] = (key, ed_y, ed_x)
    
    dist, st_y, st_x = bfs(r,c,target) # 제일 가까운 녀석의 st_y, st_x
    # st_y, st_x 로 저장한 positon에서 도착위치 꺼냄

    if fuel >= dist and dist != -1: # 승객을 태우러 감
        key, ed_y, ed_x = postion[(st_y, st_x)]
        r,c = st_y, st_x
        fuel -= dist
    else:
        print(-1)
        break
    target.clear()
    target.add((ed_y, ed_x))
    target_dist, cur_r, cur_c = bfs(r, c, target)

    # 승객 태우고 목적지로
    if fuel >= target_dist and target_dist != -1:
        r,c = ed_y, ed_x
        # 이동한 만큼 빼고, 두배 충전
        fuel += target_dist
        del customers[key]

    else:
        print(-1)
        break
else:
    print(fuel)